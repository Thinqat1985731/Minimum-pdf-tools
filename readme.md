
<div align="center">
<img src="./images/icon_.png" width="665" alt="Logo"><br>

![GitHub License](https://img.shields.io/github/license/Thinqat1985731/Minimum-pdf-tools?style=for-the-badge)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Thinqat1985731/Minimum-pdf-tools?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/Thinqat1985731/Minimum-pdf-tools?style=for-the-badge)
![GitHub tag (with filter)](https://img.shields.io/github/v/tag/Thinqat1985731/Minimum-pdf-tools?style=for-the-badge&label=Version)
</div>
<br>

pypdfによるPDF結合・分割/GhostscriptによるPDF圧縮にちょっとしたUIを付けるツール（初期はPyPDF2を検討しておりましたが、[PyPDF2のPypiサイト](https://pypi.org/project/PyPDF2/)によれば「v3.0.X（2022/12/31リリース）で開発を停止してルーツであるpypdfで開発を続ける」とのことだったので、pypdfを利用しています）。

## Requirement

- pypdf
- send2trash
- charset-normalizer
- chardet

## Usage

Requirementにあるパッケージを入れたPython環境（仮想でも生でもよい）とGhostscriptをまずは用意し、そのうえでsrcに入っているmain.pyを実行する。そうすればTkinterによるダイアログがぼちぼち出てくるのでそれに従う感じ。

## Features

- 単一のmain.pyからツールの分岐を行う。
- 順番を指定してPDFを結合することができる。
  - 上書き時の動作は保障できません。ご注意ください。
- 結合後の元PDFの削除およびGhostscriptによる結合結果PDFの圧縮に対応。
- PDFを1ページ毎または指定した境界で分離することができる。
- GhostscriptによるPDFの圧縮にUIを付与。

## History

2023/4/2  (**v1.00**)

- **公開**

2023/4/3  (v1.01)

- データが無いときの処理を追加
- Python自体の終了処理を追加
- readme.md修正

2023/4/4  (v1.10)

- 個々の作業を関数にしてパッケージ化
- 読み込みの仕様により逆順になる場合に対しての並べ替え機能追加
- 上記に伴う確認メッセージ追加
- Python自体の終了処理をより追加 (削除時のCOM surrogate防止)

2023/10/22  (**v2.00**)

- **GhostScriptにUIを付けるためのpdf-compressor追加**
- gitignoreを追加

2023/10/23

- linter/formatterでコードを整理

2023/11/03

- MITライセンスの付与
- .gitignore/readme.md修正

2023/11/09  (v2.10)

- isortでモジュール整理
- 結合後に圧縮/結合元ファイルのゴミ箱送りのオプションを追加

2023/11/10  (v2.20)

- GhostScriptの圧縮の設定をいじるウィンドウを追加

2023/11/11  (v2.30)

- 上書きする際のSend2trash回避処理の追加
- 不要コードの削除
- 変数名・コードの統一

2023/11/18  (**v3.00**)

- **3ツールを1つのmain.pyに統一し選択式へ**

2023/12/11  (v3.10)

- ロゴを追加

2023/12/13

- main.pyの誤植によるバグ修正
- readme.md更新

2023/12/21  (**v4.00**)

- **結合について、並べ替えの順番を任意に決定可能に**
- 結合後のオプションをmerging関数に統合
- readme.md更新

2023/12/22  (v4.10)

- ×ボタンが押されたときのバグ防止
- ボタンサイズや位置の改良
- Python自体の終了処理を更に追加
- 結合時に空白のページを追加できる機能を追加
- readme.md更新（Sheild.ioによるバッジ追加）

2023/12/26  (v4.20)

- 空白のページの削除に対応
- 空白のページが先頭に並んでいた場合の特殊処理を追加

2024/01/06 (**v5.00**)

- **特定の枚数でまとめた分割の対応/圧縮と分割に関して単一のファイルを読み込むように修正**
- pdf-compressorのダイアログが複数間違っていたため修正
- 圧縮関係における名前の埋め込みをf-strings（フォーマット文字列リテラル）へ変更
- mergerのほうでもwith構文が使われるようにコードを統一

2024/01/14 (v5.10)

- f-stringsでエラーが発生したため、元に戻す
- tkinterによるウィンドウのresizableを縦横ともにFalseに設定
- icon.pngが正方形に近くなるように整形

2024/01/25 (v5.20)

- pdf-compressorにfaviconのコードが残ってエラーになっていたので削除
- pdf-mergerが終了しないバグを修正

2024/02/11

- readme.mdのコードを整理

2024/02/13

- 画像をフォルダに移動

2024/02/19

- Requirementからcchardetを削除
- Python自体の終了処理を更に追加

## Author

<div align="center">
<img src="https://avatars.githubusercontent.com/u/113882060?v=4" width="100" height="100" alt="avator"><br>
<strong>Thinqat(Thinqat1985731)</strong>
</div>

## Lisence

This project is licensed under the MIT License, see the LICENSE file for details
