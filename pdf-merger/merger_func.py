# Standard Library
import os
import subprocess
import sys
from tkinter import Tk, filedialog, messagebox

# Third Party Library
from pypdf import PdfWriter
from send2trash import send2trash

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
    * 状況によりmergingに行かずにchecking段階で処理を終わらせる
    """
    files_found = ""
    for file_name in files_read:
        files_found = files_found + file_name + "\n"

    if files_read != "":  # ファイルが存在する場合
        reverse = messagebox.askquestion(
            "Pdf-merger",
            "現在の状態では以下の" + str(len(files_read)) + "個のファイルが以下の順番で結合されます：\n" + files_found + "\n逆順に並べ替えますか?",
        )

        if reverse == "yes":
            files_read = list(reversed(files_read))
        else:
            files_read = files_read

        files_found = ""
        for file_name in files_read:
            files_found = files_found + file_name + "\n"

        ok = messagebox.askokcancel(
            "Pdf-merger", "以下の" + str(len(files_read)) + "個のファイルを以下の順番で結合します：\n" + files_found + "\nよろしければ、OKを押してください。"
        )

        if ok:
            return files_read

        else:
            messagebox.showinfo("Pdf-merger", "キャンセルされました。\n最初からやり直してください。")
            root.destroy()
            sys.exit()

    else:
        messagebox.showerror("Pdf-merger", "データが選択されていません。\n最初からやり直してください。")
        root.destroy()
        sys.exit()


def merging(files_read):
    """
    結合の本体
    """
    pdf_file_merger = PdfWriter()
    for pdf in files_read:
        pdf_file_merger.append(pdf)

    file_name_save = filedialog.asksaveasfilename(
        title="結合したファイルを名前を付けて保存", filetypes=[("PDF file", "*.pdf")], initialdir=iDir
    )

    if file_name_save.rfind(".pdf") == -1:
        file_name_save = file_name_save + ".pdf"
        # 右から検索して.pdfが無かったら勝手に付け足す

    pdf_file_merger.write(file_name_save)
    pdf_file_merger.close()  # writer を閉じる

    return file_name_save


def option(files_read, file_name_save):
    """
    結合後のオプション機能
    """
    delete = messagebox.askquestion(
        "Pdf-merger",
        "結合に使用したPDFをゴミ箱に移動しますか？",
    )

    if delete == "yes":
        for file_name in files_read:
            file_name_delete = file_name.replace("/", "\\")  # get_short_path_name() に対応
            send2trash(file_name_delete)

    compress = messagebox.askquestion(
        "Pdf-merger",
        "結合後のPDFを圧縮しますか？（GhostScriptが必要）",
    )

    if compress == "yes":
        file_name_temp = file_name_save.replace(".pdf", "_.pdf")
        subprocess.check_output(
            [
                "gswin64c",
                "-sDEVICE=pdfwrite",
                "-dPDFSETTINGS=/default",
                "-dBATCH",
                "-dNOPAUSE",
                "-dSAFER",
                "-sOUTPUTFILE=%s" % (file_name_temp,),
                file_name_save,
            ]
        )
        os.remove(file_name_save)
        file_name_temp.replace("_.pdf", ".pdf")

    messagebox.showinfo("Pdf-merger", "処理が完了しました。")
    root.destroy()
    return
