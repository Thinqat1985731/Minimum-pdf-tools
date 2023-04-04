# Pdf-tools

## Overview
pypdfを使ってみたかっただけのガバガバツールです（初期はPyPDF2を検討しておりましたが、[PyPDF2のPypiサイト](https://pypi.org/project/PyPDF2/)によれば「v3.0.X（2022/12/31リリース）で開発を停止してルーツであるpypdfで開発を続ける」とのことだったので、pypdfを利用しています）。

## Requirement
- pypdf

## Usage
Tkinterで何とかダイアログ化したのでそれに従う感じです。上書きしようとするとバグります (これに関しては対応策検討中)。

## Features
データが無いときに警告したり、pdf-mergerで保存時に.pdf付け忘れた場合に勝手に付け足すくらいしかないです。あとは巷に転がっている感じのやつ。

## Author
<div style="text-align: center;">
<img src="https://avatars.githubusercontent.com/u/113882060?v=4" width="20%"><br>
<strong>Thinqat(Thinqat1985731)</strong>
</div>

## History
2023/4/2
* 公開

2023/4/3
* データが無いときの処理追加
* Python自体の終了処理追加
* readme.md修正

2023/4/4
* 個々の作業を関数にしてパッケージ化
* 読み込みの仕様により逆順になる場合に対応した並べ替え処理追加
* メッセージによる確認をより厳重に変更