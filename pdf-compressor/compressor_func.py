# Standard Library
import os
import subprocess
import sys
from tkinter import Button, Label, Radiobutton, StringVar, Tk, filedialog, messagebox

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
    ghostscriptを拝借した圧縮の本体。設定ウィンドウもあるよ。
    """
    root_s = Tk()
    root_s.geometry('250x240')
    root_s.title("pdf-compressor")

    radio_var = StringVar(root_s)

    radio1 = Radiobutton(
        root_s,
        value="/default",
        variable=radio_var,
        text="/default"
    )
    radio1.pack()
    radio1.place(x=20, y=60)

    radio2 = Radiobutton(
        root_s,
        value="/screen",
        variable=radio_var,
        text="/screen"
    )
    radio2.pack()
    radio2.place(x=20, y=82)

    radio3 = Radiobutton(
        root_s,
        value="/ebook",
        variable=radio_var,
        text="/ebook"
    )
    radio3.pack()
    radio3.place(x=20, y=104)

    radio4 = Radiobutton(
        root_s,
        value="/printer",
        variable=radio_var,
        text="/printer"
    )
    radio4.pack()
    radio4.place(x=20, y=126)

    radio5 = Radiobutton(
        root_s,
        value="/prepress",
        variable=radio_var,
        text="/prepress"
    )
    radio5.pack()
    radio5.place(x=20, y=148)

    def btn_click():
        root_s.quit()
        root_s.destroy()

    label = Label(root_s, text="圧縮の設定を選んでください。")
    label.pack()
    label.place(x=20, y=10)

    button = Button(
        root_s,
        text="OK",
        command=btn_click
    )
    button.place(x=20, y=180)

    root_s.mainloop()

    print(radio_var.get())

    for file_name in files_read:
        pdf_file_name = file_name.replace(".pdf", "_compressed.pdf")
        subprocess.check_output(
            [
                "gswin64c",
                "-sDEVICE=pdfwrite",
                "-dPDFSETTINGS=%s" % (radio_var.get()),
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
