# Standard Library
import os
import subprocess
import sys
from tkinter import Button, Label, Radiobutton, StringVar, Tk, messagebox

root = Tk()
root.withdraw()


def compressor_check(file_read):
    """
    読み込んだファイルのリストの結合前処理（存在の確認や並べ替えなど）
    処理後のリストを返す
    * 状況によりcheck段階で処理を終わらせる
    """
    if file_read != "":  # ファイルが存在する場合
        ok = messagebox.askokcancel(
            "pdf-compressor",
            "以下のファイルを圧縮します：\n"
            + file_read
            + "\nよろしければ、OKを押してください。",
        )

        if ok:
            return file_read

        else:
            messagebox.showinfo(
                "pdf-compressor",
                "キャンセルされました。\n最初からやり直してください。",
            )
            root.destroy()
            sys.exit()

    else:
        messagebox.showerror(
            "pdf-compressor",
            "データが選択されていません。\n最初からやり直してください。",
        )
        root.destroy()
        sys.exit()


def compressing(file_read):
    """
    ghostscriptを拝借した圧縮の本体。設定ウィンドウもあるよ。
    """
    root_s = Tk()
    root_s.geometry("250x240")
    root_s.title("pdf-compressor")

    radio_var = StringVar(root_s)

    radio1 = Radiobutton(
        root_s, value="/default", variable=radio_var, text="/default"
    )
    radio1.pack()
    radio1.place(x=20, y=60)

    radio2 = Radiobutton(
        root_s, value="/screen", variable=radio_var, text="/screen"
    )
    radio2.pack()
    radio2.place(x=20, y=82)

    radio3 = Radiobutton(
        root_s, value="/ebook", variable=radio_var, text="/ebook"
    )
    radio3.pack()
    radio3.place(x=20, y=104)

    radio4 = Radiobutton(
        root_s, value="/printer", variable=radio_var, text="/printer"
    )
    radio4.pack()
    radio4.place(x=20, y=126)

    radio5 = Radiobutton(
        root_s, value="/prepress", variable=radio_var, text="/prepress"
    )
    radio5.pack()
    radio5.place(x=20, y=148)

    radio_var.set("/default")

    def btn_click():
        root_s.quit()
        root_s.destroy()

    def click_close():
        messagebox.showinfo(
            "pdf-compressor",
            "キャンセルされました。\n最初からやり直してください。",
        )
        root_s.destroy()
        root.destroy()
        sys.exit()

    label = Label(root_s, text="圧縮の設定を選んでください。")
    label.pack()
    label.place(x=20, y=10)

    button = Button(root_s, text="OK", command=btn_click)
    button.place(x=125, y=180, width=100)

    root_s.protocol("WM_DELETE_WINDOW", click_close)
    root_s.mainloop()

    replace = messagebox.askquestion(
        "pdf-compressor",
        "圧縮前のファイルを削除しますか？",
    )

    for file_name in file_read:
        if replace == "yes":
            file_name_temp = file_name.replace(".pdf", "_.pdf")
            subprocess.check_output(
                [
                    "gswin64c",
                    "-sDEVICE=pdfwrite",
                    f"-dPDFSETTINGS={radio_var.get()}",
                    "-dBATCH",
                    "-dNOPAUSE",
                    "-dSAFER",
                    f"-sOUTPUTFILE={file_name_temp,}",
                    file_name,
                ]
            )
            os.remove(file_name)
            os.rename(file_name_temp, file_name)
        else:
            file_name_save = file_name.replace(".pdf", "_compressed.pdf")
            subprocess.check_output(
                [
                    "gswin64c",
                    "-sDEVICE=pdfwrite",
                    f"-dPDFSETTINGS={radio_var.get()}",
                    "-dBATCH",
                    "-dNOPAUSE",
                    "-dSAFER",
                    f"-sOUTPUTFILE={file_name_save,}",
                    file_name,
                ]
            )

    messagebox.showinfo("pdf-compressor", "処理が完了しました。")
    root.destroy()
    return
