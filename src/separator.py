# Standard Library
import ctypes
import os
from tkinter import (
    END,
    Button,
    Frame,
    Label,
    Listbox,
    Scrollbar,
    Tk,
    messagebox,
)
from zoneinfo import ZoneInfo

# Third Party Library
from pypdf import PdfReader, PdfWriter

from common import metamaker

ctypes.windll.shcore.SetProcessDpiAwareness(1)
root = Tk()
root.withdraw()


def separating(file_read: str, tzinfo: list[ZoneInfo, str]) -> None:
    """
    分離の本体
    """
    (name, _) = os.path.splitext(file_read)  # 拡張子を分離
    pdf_file_reader = PdfReader(file_read)
    meta = pdf_file_reader.metadata  # メタデータを取得

    onebyone = messagebox.askquestion(
        "pdf-separator",
        "1ページ毎に分割しますか？"
        + "\n（「いいえ」を押すと、境界の設定に移行します）",
    )

    if onebyone == "yes":
        for num, file_object in enumerate(pdf_file_reader.pages):
            pdf_name = name + "-" + str(num + 1) + ".pdf"
            pdf_file_writer = PdfWriter()
            with open(pdf_name, "wb") as file:
                pdf_file_writer.add_page(
                    file_object
                )  # 書き出したいデータを追加
                new_meta = metamaker(tzinfo, meta)
                pdf_file_writer.add_metadata(new_meta)
                pdf_file_writer.write(file)  # openしたファイルに書き込む
                # with構文によりプログラムの終了時に自動的に閉じられる

        pdf_file_writer.close()  # writerを閉じる
        messagebox.showinfo("pdf-separator", "処理が完了しました。")
        root.quit()
        root.destroy()

    else:
        root_o = Tk()

        root_o.geometry("600x350")
        root_o.resizable(False, False)
        root_o.title("pdf-separator")

        def up_list() -> None:  # 選択したファイルを1つ前に
            indices = listbox.curselection()
            if len(indices) == 1:  # 選択した項目が１つか？
                if listbox.get(indices) == "-----------------":
                    if indices[0] > 0:
                        listbox.insert(indices[0] - 1, listbox.get(indices))
                        listbox.delete(indices[0] + 1)
                        listbox.select_set(indices[0] - 1)

        def down_list() -> None:  # 選択したファイルを1つ後に
            indices = listbox.curselection()
            if len(indices) == 1:  # 選択した項目が１つか？
                if listbox.get(indices) == "-----------------":
                    if indices[0] < listbox.size() - 1:
                        listbox.insert(indices[0] + 2, listbox.get(indices))
                        listbox.delete(indices)
                        listbox.select_set(indices[0] + 1)

        def add_line() -> None:  # 選択したファイルの1つ後に空白ページを追加
            indices = listbox.curselection()
            if len(indices) == 1:  # 選択した項目が１つか？
                listbox.insert(indices[0] + 1, "-----------------")

        def delete_line() -> None:  # 選択したファイルの1つ後に空白ページを追加
            indices = listbox.curselection()
            if len(indices) == 1:  # 選択した項目が１つか？
                if listbox.get(indices) == "-----------------":
                    listbox.delete(indices[0])

        def btn_click_ok() -> None:
            # 境界の場所を確認し、分割用の二重配列を作成する。
            file_num = 0
            page_n_temp = 0
            pages_one_file = []
            pages = []

            for num in range(listbox.size()):
                if listbox.get(num) == "-----------------":
                    pages.append(pages_one_file)
                    pages_one_file = []
                else:
                    pages_one_file.append(page_n_temp)
                    page_n_temp = page_n_temp + 1
            pages.append(pages_one_file)  # 最後に1個は作成

            for file_contents in pages:
                pdf_name = name + "-" + str(file_num + 1) + ".pdf"
                pdf_file_writer = PdfWriter()
                with open(pdf_name, "wb") as file:
                    for page_num in file_contents:
                        file_object = pdf_file_reader.pages[page_num]
                        pdf_file_writer.add_page(file_object)
                    new_meta = metamaker(tzinfo, meta)
                    pdf_file_writer.add_metadata(new_meta)
                    pdf_file_writer.write(file)  # openしたファイルに書き込む
                    # with構文によりプログラムの終了時に自動的に閉じられる
                file_num = file_num + 1

            pdf_file_writer.close()  # writerを閉じる
            messagebox.showinfo("pdf-separator", "処理が完了しました。")

            root_o.quit()
            root_o.destroy()
            root.quit()
            root.destroy()

        def click_close() -> None:
            messagebox.showinfo(
                "pdf-separator",
                "キャンセルされました。\n最初からやり直してください。",
            )
            root_o.quit()
            root_o.destroy()
            root.quit()
            root.destroy()

        # フレームの生成
        frame = Frame(root_o)
        frame.place(x=20, y=30)

        # Listboxウィジェットを生成し、読み込んだファイルを入れる
        listbox = Listbox(frame, width=62, height=12, selectmode="signal")
        for num in range(len(pdf_file_reader.pages)):
            page = file_read + "-" + str(num + 1) + ".pdf"
            listbox.insert(END, page)
        listbox.pack(fill="x", side="left")

        # スクロールバーの生成
        scroll = Scrollbar(frame, orient="vertical")
        listbox.configure(yscrollcommand=scroll.set)
        scroll.config(command=listbox.yview)
        scroll.pack(side="right", fill="y")

        # ラベルの配置
        label = Label(
            root_o,
            text="分割境界を設定してください（境界の部分で分割します）。",
        )
        label.pack()
        label.place(x=20, y=3)

        # ボタンを定義して配置
        button_add_page = Button(
            root_o, text="分割の境界を追加", command=add_line
        )
        button_delete_page = Button(
            root_o, text="分割の境界を削除", command=delete_line
        )
        button_ok = Button(root_o, text="分割", command=btn_click_ok)
        button_up = Button(root_o, text="▲", command=up_list)
        button_down = Button(root_o, text="▼", command=down_list)

        button_add_page.place(x=135, y=300, width=150)
        button_delete_page.place(x=305, y=300, width=150)
        button_ok.place(x=475, y=300, width=100)
        button_up.place(x=550, y=100, width=40)
        button_down.place(x=550, y=150, width=40)

        root_o.protocol("WM_DELETE_WINDOW", click_close)
        root_o.mainloop()

    return
