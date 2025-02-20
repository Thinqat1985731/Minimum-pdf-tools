
<a id="readme-top"></a>

<div align="center">
<picture>
  <source
    srcset="./images/icon2_dark.png"
    alt="Typing SVG"
    media="(prefers-color-scheme: dark)"
  />
  <source
    srcset="./images/icon2_light.png"
    alt="Typing SVG"
    media="(prefers-color-scheme: light)"
  />
  <img src="./images/icon2_ldark.png" width="665" alt="Logo">
</picture>
<br>

![GitHub License](https://img.shields.io/github/license/Thinqat1985731/Minimum-pdf-tools?style=for-the-badge&color=C6E1E4)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Thinqat1985731/Minimum-pdf-tools?style=for-the-badge&color=C6E1E4)
![GitHub repo size](https://img.shields.io/github/repo-size/Thinqat1985731/Minimum-pdf-tools?style=for-the-badge)
![GitHub tag (with filter)](https://img.shields.io/github/v/tag/Thinqat1985731/Minimum-pdf-tools?style=for-the-badge&label=Version)
</div>
<br>

<details>
  <summary>Table of Contents</summary>

- [About This Project](#about-this-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [History](#history)
- [Lisence](#lisence)
- [Contact](#contact)

</details>

## About This Project

pypdfによるPDF結合・分割/GhostscriptによるPDF圧縮にちょっとしたUIを付けるツールです。特徴といえそうなのは以下です。

- 単一の`main.py`からツールの分岐を行う。
- 順番を指定してPDFを結合することができる。
  - 上書き時の動作は保障できません。ご注意ください。
- 結合後の元PDFの削除およびGhostscriptによる結合結果PDFの圧縮に対応。
- PDFを1ページ毎または指定した境界で分離することができる。
- GhostscriptによるPDFの圧縮にUIを付与。

> 初期はPyPDF2を検討しておりましたが、[PyPDF2のPypiサイト](https://pypi.org/project/PyPDF2/)によれば「v3.0.X（2022/12/31リリース）で開発を停止してルーツであるpypdfで開発を続ける」とのことだったので、pypdfを利用しています。

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

- 仮想環境での動作を想定しています。

  ```shell
  python -m venv ci_env
  (for linux  ) source ci_env/bin/activate
  (for windows) .\ci_env\Scripts\activate
  ```

- PDFの圧縮において、**GhostScript**が存在する前提で組んでいるため、事前にインストールが必要です。
公式のインストールページは[こちら](https://ghostscript.com/releases/gsdnld.html)。

### Installation

1. このリポジトリをクローンする。

     ```shell
     git clone https://github.com/Thinqat1985731/Minimum-pdf-tools.git
     ```

2. 関連するpythonライブラリをインストールする。

    ```shell
     pip install pypdf
     pip install charset-normalizer
     pip install chardet
     pip install send2trash
     pip install tzdata 
    ```

    > PoetryやRyeでtomlファイルを作成し、インストールしても可。

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

src内の`main.py`を実行する。そうすればTkinterによるダイアログがぼちぼち出てくるのでそれに従う感じ。

```shell
cd src
python main.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## History

2023/4/3  (**v1.0.0**)

- **公開**

2023/4/3  (v1.1.0)

- **データが無いときの処理を追加**
- Python自体の終了処理を追加
- `readme.md`修正

2023/4/4  (v1.2.0)

- **読み込みの仕様により逆順になる場合に対しての並べ替え機能追加**
- **個々の作業を関数にしてパッケージ化/確認メッセージ追加**
- Python自体の終了処理をより追加 (削除時のCOM surrogate防止)

2023/10/22  (**v2.0.0**)

- **GhostScriptにUIを付けるためのpdf-compressor追加**
- `.gitignore`を追加

2023/10/23

- linter/formatterでコードを整理

2023/11/03

- MITライセンスの付与
- `.gitignore`/`readme.md`修正

2023/11/09  (v2.1.0)

- **結合後に圧縮/結合元ファイルのゴミ箱送りのオプションを追加**
- isortでモジュール整理

2023/11/10  (v2.2.0)

- **GhostScriptの圧縮の設定をいじるウィンドウを追加**

2023/11/11  (v2.3.0)

- **上書きする際のSend2trash回避処理の追加**
- 不要コードの削除
- 変数名・コードの統一

2023/11/18  (**v3.0.0**)

- **3ツールを1つの`main.py`に統一し選択式へ**

2023/12/11

- ロゴを追加

2023/12/13 (v3.0.1)

- `main.py`の誤植によるバグ修正

2023/12/21  (**v4.0.0**)

- **結合について、並べ替えの順番を任意に決定可能に**
- 結合後のオプションをmerging関数に統合

2023/12/22  (v4.1.0)

- **結合時に空白のページを追加できる機能を追加**
- ×ボタンが押されたときのバグ防止/ボタンサイズや位置の改良
- Python自体の終了処理を追加
- `readme.md`にSheild.ioによるバッジ追加

2023/12/26  (v4.2.0)

- **空白のページの削除や空白のページが先頭に並んでいた場合に対応**

2024/01/06 (**v5.0.0**)

- **特定の枚数でまとめた分割の対応/圧縮と分割に関して単一のファイルを読み込むように修正**
- pdf-compressorのダイアログが複数間違っていたため修正
- 圧縮関係における名前の埋め込みをf-strings（フォーマット文字列リテラル）へ変更
- mergerのほうでもwith構文が使われるようにコードを統一

2024/01/14 (v5.0.1)

- f-stringsでエラーが発生したため、元に戻す
- tkinterによるウィンドウのresizableを縦横ともにFalseに設定
- `icon.png`が正方形に近くなるように整形

2024/01/25 (v5.0.2)

- pdf-compressorにfaviconのコードが残ってエラーになっていたので削除
- pdf-mergerが終了しないバグを修正

2024/02/11

- `readme.md`のコードを整理

2024/02/13

- 画像をフォルダに移動

2024/02/19 (v5.0.3)

- Requirementからcchardetを削除
- Python自体の終了処理を追加

2024/02/22

- 型ヒント追加/余剰コードの削除

2024/03/01 (v5.1.0)

- **データの読み込み/前処理をpreprocessor.pyとして分離。**
- **pdf-separator/pdf-compressorにおいてpypdfが生成ツールになるのを避けるため、メタデータ保存を実装。**
- ツール分岐に際してのバグ修正

2024/03/08 (v5.1.1)

- \_\_name\_\_ ==\_\_main\_\_の際の処理追加
- バグ・ライブラリ分類の修正

2024/04/04 (v5.1.2)

- ウィンドウの解像度向上とそれに伴う調整
- 終了処理の見直し

2024/04/05

- コードの修正

2024/04/09 (v5.2.0)

- **作成ソフトのメタデータが存在しないファイルの対応**

2024/04/29

- 不要な変数・記述の削除

2024/06/22

- `readme.md`に目次・ディレクトリ構造を追加

2024/06/30

- `readme.md`の構成を大幅に変更

2025/02/20 (**v6.0.0**)

- **時間の設定を追加し、メタデータの保存を大幅に改良**
- `preprocess.py`→`common.py`として時間設定とメタデータ処理を共有
- `readme.md`のブログリンク変更と説明追加・表記更新
- version表記を変更

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Lisence

This project is licensed under the MIT License, see the [LICENSE file](LICENSE) for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

<div align="center">
   <img src="https://avatars.githubusercontent.com/u/113882060?v=4" width="100" height="100" alt="avator"><br>
   <strong>Thinqat(Thinqat1985731)</strong><br><br>

  <a href="https://github.com/Thinqat1985731" target="_blank">
  <picture>
    <source
      srcset="https://img.shields.io/badge/GitHub-444444.svg?style=for-the-badge&logo=github"
      media="(prefers-color-scheme: dark)"
    />
    <source
      srcset="https://img.shields.io/badge/GitHub-000000.svg?style=for-the-badge&logo=github"
      media="(prefers-color-scheme: light)"
    />
    <img src="https://img.shields.io/badge/-Github-444444.svg?style=for-the-badge&logo=github" alt="Github"/>
  </picture>
  </a>
  <a href="https://huggingface.co/Thinqat1985731" target="_blank">
    <picture>
      <source
        srcset="https://img.shields.io/badge/Hugging_Face-444444.svg?style=for-the-badge&logo=huggingface&logoColor=white"
        media="(prefers-color-scheme: dark)"
      />
      <source
        srcset="https://img.shields.io/badge/Hugging_Face-000000.svg?style=for-the-badge&logo=huggingface&logoColor=white"
        media="(prefers-color-scheme: light)"
      />
      <img src="https://img.shields.io/badge/Hugging_Face-444444.svg?style=for-the-badge&logo=huggingface&logoColor=white" alt="Hugging Face"/>
    </picture>
  </a>
  <a href="https://thinqat1985731.github.io/myblog/" target="_blank">
    <picture>
      <source
        srcset="https://img.shields.io/badge/Myblog-444444.svg?style=for-the-badge&logo=jekyll"
        media="(prefers-color-scheme: dark)"
      />
      <source
        srcset="https://img.shields.io/badge/Myblog-000000.svg?style=for-the-badge&logo=jekyll"
        media="(prefers-color-scheme: light)"
      />
      <img src="https://img.shields.io/badge/Myblog-444444.svg?style=for-the-badge&logo=jekyll" alt="Myblog"/>
    </picture>
  </a>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
