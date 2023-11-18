# Standard Library
import os
import sys
from tkinter import (
    Tk,
    filedialog,
    messagebox,
)

dirname = os.path.dirname(__file__)
iDir = os.path.abspath(dirname)
root = Tk()
root.withdraw()


def files_reading():
    """
    ファイルの読み込み
    読み込まれたファイルのリストを返す
    """
    files_read = filedialog.askopenfilenames(
        title="開く", filetypes=[("PDF file", "*.pdf")], initialdir=iDir
    )

    return files_read


def checking(files_read, program):
    """
    読み込んだファイルのリストの結合前処理（存在の確認や並べ替えなど）
    処理後のリストを返す
    * 状況によりchecking段階で処理を終わらせる
    """
    files_found = ""
    for file_name in files_read:
        files_found = files_found + file_name + "\n"

    if files_read != "":  # ファイルが存在する場合
        if program == "pdf-merger":
            reverse = messagebox.askquestion(
                program,
                "現在の状態では以下の"
                + str(len(files_read))
                + "個のファイルが以下の順番で結合されます：\n"
                + files_found
                + "\n逆順に並べ替えますか?",
            )

            if reverse == "yes":
                files_read = list(reversed(files_read))
            else:
                files_read = files_read

            files_found = ""
            for file_name in files_read:
                files_found = files_found + file_name + "\n"

            ok = messagebox.askokcancel(
                program,
                "以下の"
                + str(len(files_read))
                + "個のファイルを以下の順番で結合します：\n"
                + files_found
                + "\nよろしければ、OKを押してください。",
            )

        elif program == "pdf-separator":
            ok = messagebox.askokcancel(
                "Pdf-separator",
                "以下の"
                + str(len(files_read))
                + "個のファイルを個々のページに分割します：\n"
                + files_found
                + "\nよろしければ、OKを押してください。",
            )

        elif program == "pdf-compressor":
            ok = messagebox.askokcancel(
                program,
                "以下の"
                + str(len(files_read))
                + "個のファイルを圧縮します：\n"
                + files_found
                + "\nよろしければ、OKを押してください。",
            )

        if ok:
            return files_read

        else:
            messagebox.showinfo(
                program,
                "キャンセルされました。\n最初からやり直してください。",
            )
            root.destroy()
            sys.exit()

    else:
        messagebox.showerror(
            program,
            "データが選択されていません。\n最初からやり直してください。",
        )
        root.destroy()
        sys.exit()
