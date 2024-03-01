# Standard Library
import os
import sys
from tkinter import filedialog, messagebox

dirname = os.path.dirname(__file__)
iDir = os.path.abspath(dirname)


def dataloader(tool: str) -> list[str] | str:
    if tool == "pdf-merger":
        # 複数PDFファイルを開く
        files_read = filedialog.askopenfilenames(
            title="開く", filetypes=[("PDF file", "*.pdf")], initialdir=iDir
        )
    else:
        # 単一PDFファイルを開く
        files_read = filedialog.askopenfilename(
            title="開く", filetypes=[("PDF file", "*.pdf")], initialdir=iDir
        )
    return files_read


def startcheck(tool: str, files_read: list[str] | str) -> None:
    if files_read != "":  # ファイルが存在する場合
        files_found = ""
        for file_name in files_read:
            files_found = files_found + file_name + "\n"

        if tool == "pdf-merger":
            ok = messagebox.askokcancel(
                tool,
                "以下の"
                + str(len(files_read))
                + "個のファイルを結合します：\n"
                + files_found
                + "\nよろしければ、OKを押してください"
                + "\n（OKを押すと、結合順の設定に移行します）。",
            )
        elif tool == "pdf-separator":
            ok = messagebox.askokcancel(
                tool,
                "以下のファイルを分割します：\n"
                + files_read
                + "\nよろしければ、OKを押してください。",
            )
        else:
            ok = messagebox.askokcancel(
                tool,
                "以下のファイルを圧縮します：\n"
                + files_read
                + "\nよろしければ、OKを押してください。",
            )

        if ok:
            return
        else:
            messagebox.showinfo(
                tool,
                "キャンセルされました。\n最初からやり直してください。",
            )
            sys.exit()

    else:
        messagebox.showerror(
            tool,
            "データが選択されていません。\n最初からやり直してください。",
        )
        sys.exit()
