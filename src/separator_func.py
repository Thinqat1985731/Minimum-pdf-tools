# Standard Library
import os
from tkinter import Tk, messagebox

# Third Party Library
from pypdf import PdfReader, PdfWriter

root = Tk()
root.withdraw()


def separating(files_read):
    """
    分離の本体
    """
    for file_name in files_read:
        (name, extention) = os.path.splitext(file_name)  # 拡張子を分離
        pdf_file_reader = PdfReader(file_name)
        page_n = len(pdf_file_reader.pages)  # ページ数を取得

        for num in range(page_n):
            file_object = pdf_file_reader.pages[
                num
            ]  # 指定ページの内容だけ抜き出す
            pdf_file_name = name + "-" + str(num + 1) + ".pdf"
            pdf_file_writer = PdfWriter()
            with open(pdf_file_name, "wb") as file:
                pdf_file_writer.add_page(
                    file_object
                )  # 書き出したいデータを追加
                pdf_file_writer.write(file)  # openしたファイルに書き込む
                # with構文によりプログラムの終了時に自動的に閉じられる

    pdf_file_writer.close()  # writerを閉じる

    messagebox.showinfo("Pdf-separator", "処理が完了しました。")
    root.destroy()
    return
