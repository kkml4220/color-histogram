import cv2
import os
import sys

import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR_NAME = "output"

# 出力ファイルの画像形式
OUTPUT_IMAGE_EXTENTION = "png"

# openCV imwriteの仕様により指定できるフォーマットは限定されています
# 詳しくはopenCV imwriteのドキュメントをご確認ください
# URL: https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce


def normalize_path(path):
    """パスを正規化する
    Unix系のOSでは"/"を使うがWindowsでは"\\"を使うため,
    これを"/"に正規化する
    """
    return os.path.normpath(path.replace('/', '\\'))


def is_absolute_path(path):
    """パスが絶対パスか判定"""
    return os.path.isabs(path)


def get_inputfile_abs_path(path):
    """入力ファイルのパスの絶対パスを取得
    Returns (str): 入力ファイルの絶対パスを返す
    """

    # 入力が絶対パスかどうか判定
    if not is_absolute_path(path):
        absolute_path = os.path.abspath(path)
    else:
        absolute_path = path

    if not os.path.exists(absolute_path):
        raise FileNotFoundError(f"{absolute_path} が見つかりません")

    return absolute_path


def get_output_dir_path():
    """outputディレクトリの絶対パス
        Return (str): このスクリプトと同階層にあるoutputディレクトリの絶対パスを返します
    """
    # このスクリプトの実行されている絶対パスのディレクトリのパスを返す
    script_abs_dir_path = os.path.dirname(__file__)
    output_dir_path = os.path.join(script_abs_dir_path, OUTPUT_DIR_NAME)

    # ouputディレクトリが存在しない場合
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
        print(f"{output_dir_path}ディレクトリを作成しました")
        return output_dir_path

    return output_dir_path


def get_file_basename_without_extention(file_path):
    """ファイルのパスから拡張子なしのファイル名を取得
    Args:
        file_path (str): ファイルの絶対パスまたは相対パス
    Returns (str) : ファイルパスから拡張子なしのファイル名を取得します
    """
    basename = os.path.basename(file_path)
    file_name_without_extention = os.path.splitext(basename)[0]
    return file_name_without_extention


def decorator_print_arguments_and_result(original_function):
    """引数と結果を描画するデコレータ"""
    def wrapper_function(*args, **kwargs):
        # 引数の表示
        print("=" * 60)
        print(f"引数: {args}, {kwargs}")
        # 関数の実行
        result = original_function(*args, **kwargs)
        # 結果の表示
        print(f"結果: {result}")
        print("=" * 60)

        return result
    return wrapper_function


@decorator_print_arguments_and_result
def plot_color_histogram(filepath, show=False):
    """Color histogramをプロット
    Args: 
        filepath (str) : 入力画像への絶対パス
        show (bool) : plot画像を別ウィンドウで描画するかどうかのフラグ
                    defaultでは表示しない設定
    """
    output_dir_path = get_output_dir_path()
    output_files = []

    # 画像の読み込み
    image = cv2.imread(filepath)
    filename = get_file_basename_without_extention(filepath)

    # BGRからRGBに変換
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # チャンネルごとのヒストグラムを計算
    histogram_r = cv2.calcHist([image_rgb], [0], None, [256], [0, 256])
    histogram_g = cv2.calcHist([image_rgb], [1], None, [256], [0, 256])
    histogram_b = cv2.calcHist([image_rgb], [2], None, [256], [0, 256])
    plt.figure()

    # RGBのそれぞれのヒストグラムを表示
    plt.subplot(2, 2, 1)
    plt.plot(histogram_r, color="red", alpha=0.7)
    plt.title("Red Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Frequency")

    plt.subplot(2, 2, 2)
    plt.plot(histogram_g, color="green", alpha=0.7)
    plt.title("Green Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Frequency")

    plt.subplot(2, 2, 3)
    plt.plot(histogram_b, color="blue", alpha=0.7)
    plt.title("Blue Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Frequency")

    # RGBのヒストグラムを組み合わせたヒストグラムを表示
    plt.subplot(2, 2, 4)
    plt.plot(histogram_r, color="red", alpha=0.7, label="Red")
    plt.plot(histogram_g, color="green", alpha=0.7, label="Green")
    plt.plot(histogram_b, color="blue", alpha=0.7, label="Blue")
    plt.title("Combined RGB Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Frequency")
    plt.legend()

    # 画像として保存
    plt.tight_layout()

    # 出力ファイル名を定義
    histogram_filename = f"{filename}_histograms.{OUTPUT_IMAGE_EXTENTION}"
    histogram_file_path = os.path.join(output_dir_path, histogram_filename)
    plt.savefig(histogram_file_path)
    output_files.append(histogram_file_path)

    if show:
        plt.show()

    # RGBのそれぞれのヒストグラムを画像として保存
    plt.figure()

    plt.plot(histogram_r, color="red", alpha=0.7)
    plt.title("Red Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Frequency")

    # 出力ファイル名を定義
    histogram_red_filename = (
        f"{filename}_histogram_red.{OUTPUT_IMAGE_EXTENTION}"
    )
    histogram_red_file_path = os.path.join(
        output_dir_path, histogram_red_filename)
    plt.savefig(histogram_red_file_path)
    output_files.append(histogram_file_path)

    plt.figure()

    plt.plot(histogram_g, color="green", alpha=0.7)
    plt.title("Green Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Frequency")

    # 出力ファイル名を定義
    histogram_green_filename = (
        f"{filename}_histogram_green.{OUTPUT_IMAGE_EXTENTION}"
    )
    histogram_geeen_file_path = os.path.join(
        output_dir_path, histogram_green_filename
    )
    plt.savefig(histogram_geeen_file_path)
    output_files.append(histogram_file_path)

    plt.figure()

    plt.plot(histogram_b, color="blue", alpha=0.7)
    plt.title("Blue Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Frequency")

    # 出力ファイル名を定義
    histogram_blue_filename = (
        f"{filename}_histogram_blue.{OUTPUT_IMAGE_EXTENTION}"
    )
    histogram_blue_file_path = os.path.join(
        output_dir_path, histogram_blue_filename
    )
    plt.savefig(histogram_blue_file_path)

    return output_files


class ValidationError(Exception):
    """バリデーションエラー"""

    def __init__(self, message="バリデーションエラーです"):
        self.message = message
        super().__init__(self.message)


def validation_check(input_file_path):
    """入力時のバリデーションチェック"""

    # 入力引数の絶対パスを取得
    inputfile_abs_path = get_inputfile_abs_path(
        normalize_path(input_file_path))

    # ファイルが存在するか確認
    if not os.path.exists(inputfile_abs_path):
        raise ValidationError(f"{inputfile_abs_path}が見つかりません")

    return True


def main():
    args = sys.argv
    if len(args) != 2:
        raise ValidationError("コマンドライン引数が無効です")

    # 引数の受け取り
    input_filepath = normalize_path(args[1])

    if validation_check(input_filepath):
        plot_color_histogram(input_filepath)


if __name__ == "__main__":
    main()
