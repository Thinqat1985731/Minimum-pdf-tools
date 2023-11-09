# Standard Library
import os
import subprocess
import sys
from tkinter import Tk, filedialog, messagebox

dirname = os.path.dirname(__file__)
iDir = os.path.abspath(dirname)
root = Tk()
root.withdraw()


def files_reading():
    """
    ファイルの読み込み
    読み込まれたファイルのリストを返す
    """
    files_read = filedialog.askopenfilenames(title="開く", filetypes=[("PDF file", "*.pdf")], initialdir=iDir)

    return files_read


def checking(files_read):
    """
    読み込んだファイルのリストの結合前処理（存在の確認や並べ替えなど）
    処理後のリストを返す
    * 状況によりseparatingに行かずにchecking段階で処理を終わらせる
    """
    files_found = ""

    for file_name in files_read:
        files_found = files_found + file_name + "\n"

    if files_found != "":  # ファイルが存在する場合
        ok = messagebox.askokcancel("Pdf-compressor", "以下の" + str(len(files_read)) + "個のファイルを圧縮します：\n" + files_found)

        if ok:
            return

        else:
            messagebox.showinfo("Pdf-compressor", "キャンセルされました。\n最初からやり直してください。")
            root.destroy()
            sys.exit()

    else:
        messagebox.showerror("Pdf-compressor", "データが選択されていません。\n最初からやり直してください。")
        root.destroy()
        sys.exit()


def compressing(files_read):
    """
    ghostscriptを拝借した圧縮の本体
    """
    for file_name in files_read:
        pdf_file_name = file_name.replace(".pdf", "_compressed.pdf")

        subprocess.check_output(
            [
                "gswin64c",
                "-sDEVICE=pdfwrite",
                "-dPDFSETTINGS=/default",
                "-dBATCH",
                "-dNOPAUSE",
                "-dSAFER",
                "-sOUTPUTFILE=%s" % (pdf_file_name,),
                file_name,
            ]
        )

    messagebox.showinfo("Pdf-compressor", "処理が完了しました。")
    root.destroy()
    return
