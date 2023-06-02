# color-histogram

![APM](https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat)
![Editor](https://img.shields.io/badge/-Visual%20Studio%20Code-007ACC.svg?logo=visual-studio-code&style=flat)

画像から Color histogram を取得し画像として保存

## Demo

| Original                                          | histogram                                               |
| ------------------------------------------------- | ------------------------------------------------------- |
| ![original-image](./images/sample_background.png) | ![histogram](./images/sample_background_histograms.png) |

| R-histogram                                                  | G-histogram                                                    | B-histogram                                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------- |
| ![R-histogram](./images/sample_background_histogram_red.png) | ![G-histogram](./images/sample_background_histogram_green.png) | ![B-histogram](./images/sample_background_histogram_blue.png) |

## Installation

```bash
git clone https://github.com/kkml4220/color-histogram.git
cd color-histogram
pip install -r requirements.txt
```

## Usage

```bash
python main.py input/sample_background.png
```

## Author

- 作成者 : 高橋 克征 (Takahashi Katsuyuki)
- E-mail : [Takahashi.Katsuyuki.github@gmail.com](Takahashi.Katsuyuki.github@gmail.com)

## License

"color-histogram" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
