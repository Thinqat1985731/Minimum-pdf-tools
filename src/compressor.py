# Standard Library
import os
import subprocess
import sys
from tkinter import Button, Label, Radiobutton, StringVar, Tk, messagebox

from pypdf import PdfReader, PdfWriter

root = Tk()
root.withdraw()


def compressing(file_read: str) -> None:
    """
    ghostscriptを拝借した圧縮の本体。設定ウィンドウもあるよ。
    """
    root_s = Tk()

    root_s.geometry("250x240")
    root_s.resizable(False, False)
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

    def btn_click() -> None:
        root_s.quit()
        root_s.destroy()

    def click_close() -> None:
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

    pdf_name = file_read
    pdf_file_reader = PdfReader(file_read)
    meta = pdf_file_reader.metadata  # メタデータを取得（Producer保持のため）

    if replace == "yes":
        pdf_name_temp = pdf_name.replace(".pdf", "_.pdf")
        subprocess.check_output(
            [
                "gswin64c",
                "-sDEVICE=pdfwrite",
                "-dPDFSETTINGS=%s" % (radio_var.get()),
                "-dBATCH",
                "-dNOPAUSE",
                "-dSAFER",
                "-sOUTPUTFILE=%s" % (pdf_name_temp,),
                pdf_name,
            ]
        )
        os.remove(pdf_name)
        os.rename(pdf_name_temp, pdf_name)
        pdf_file_writer = PdfWriter()
        with open(pdf_name, "wb") as file:
            for page_num in len(pdf_file_reader.pages):
                file_object = pdf_file_reader.pages[page_num]
                pdf_file_writer.add_page(file_object)
            pdf_file_writer.add_metadata(
                {"/Producer": meta.producer}
            )  # 元のメタデータで上書き
            pdf_file_writer.write(file)  # openしたファイルに書き込む
            # with構文によりプログラムの終了時に自動的に閉じられる
    else:
        pdf_name_save = pdf_name.replace(".pdf", "_compressed.pdf")
        subprocess.check_output(
            [
                "gswin64c",
                "-sDEVICE=pdfwrite",
                "-dPDFSETTINGS=%s" % (radio_var.get()),
                "-dBATCH",
                "-dNOPAUSE",
                "-dSAFER",
                "-sOUTPUTFILE=%s" % (pdf_name_save,),
                pdf_name,
            ]
        )
        pdf_file_writer = PdfWriter()
        with open(pdf_name_save, "wb") as file:
            for num in range(len(pdf_file_reader.pages)):
                file_object = pdf_file_reader.pages[num]
                pdf_file_writer.add_page(file_object)
            pdf_file_writer.add_metadata(
                {"/Producer": meta.producer}
            )  # 元のメタデータで上書き
            pdf_file_writer.write(file)  # openしたファイルに書き込む
            # with構文によりプログラムの終了時に自動的に閉じられる

    messagebox.showinfo("pdf-compressor", "処理が完了しました。")
    root.destroy()
    return
