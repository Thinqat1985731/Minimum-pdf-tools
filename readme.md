# UIadder-for-PDFtools

## Overview
pypdfによるPDF結合・分割/GhostscriptによるPDF圧縮にちょっとしたUIを付けるツール（初期はPyPDF2を検討しておりましたが、[PyPDF2のPypiサイト](https://pypi.org/project/PyPDF2/)によれば「v3.0.X（2022/12/31リリース）で開発を停止してルーツであるpypdfで開発を続ける」とのことだったので、pypdfを利用しています）。

## Requirement
  - pypdf
  - charset-normalizer
  - chardet
  - cchardet

## Usage

Requirementにあるパッケージを入れたPython環境（仮想でも生でもよい）とGhostscriptをまずは用意し、そのうえで個々のディレクトリに入っているmain.pyを実行する。そうすればTkinterによるダイアログがぼちぼち出てくるのでそれに従う感じ。<br>
mergerは保存名聞いてきますが、既にあるやつに上書きしようとするとバグります。

## Features
データが無いときに警告したり、pdf-mergerで保存時に.pdf付け忘れた場合に勝手に付け足すくらいしかないです。

## History
2023/4/2
* 公開

2023/4/3
* データが無いときの処理を追加
* Python自体の終了処理を追加
* readme.md修正

2023/4/4
* 個々の作業を関数にしてパッケージ化
* 読み込みの仕様により逆順になる場合に対しての並べ替え機能追加
* 上記に伴う確認メッセージ追加
* Python自体の終了処理をより追加 (削除時のCOM surrogate防止)

2023/10/22
* gitignoreを追加
* ghostscriptにUIを付けるためのpdf-compressor追加

2023/10/23
* linter/formatterでコードを整理

2023/11/03
* MITライセンスの付与
* .gitignore/readme.md修正

## Author
<div align="center">
<img src="https://avatars.githubusercontent.com/u/113882060?v=4" width="10%"><br>
<strong>Thinqat(Thinqat1985731)</strong>
</div>


## Lisence
This project is licensed under the MIT License, see the LICENSE file for details
