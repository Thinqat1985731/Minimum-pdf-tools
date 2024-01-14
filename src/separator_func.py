# Standard Library
import os
import sys
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

# Third Party Library
from pypdf import PdfReader, PdfWriter

root = Tk()
root.withdraw()


def separator_check(file_read):
    """
    読み込んだファイルのリストの結合前処理（存在の確認や並べ替えなど）
    処理後のリストを返す
    * 状況によりcheck段階で処理を終わらせる
    """
    if file_read != "":  # ファイルが存在する場合
        ok = messagebox.askokcancel(
            "pdf-separator",
            "以下のファイルを分割します：\n"
            + file_read
            + "\nよろしければ、OKを押してください。",
        )

        if ok:
            return file_read

        else:
            messagebox.showinfo(
                "pdf-separator",
                "キャンセルされました。\n最初からやり直してください。",
            )
            root.destroy()
            sys.exit()

    else:
        messagebox.showerror(
            "pdf-separator",
            "データが選択されていません。\n最初からやり直してください。",
        )
        root.destroy()
        sys.exit()


def separating(file_read):
    """
    分離の本体
    """
    (name, extention) = os.path.splitext(file_read)  # 拡張子を分離
    pdf_file_reader = PdfReader(file_read)
    page_n = len(pdf_file_reader.pages)  # ページ数を取得
    pdf_file_writer = PdfWriter()

    onebyone = messagebox.askquestion(
        "pdf-separator",
        "1ページ毎に分割しますか？"
        + "\n（「いいえ」を押すと、境界の設定に移行します）",
    )

    if onebyone == "yes":
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
        messagebox.showinfo("pdf-separator", "処理が完了しました。")
        root.destroy()

    else:
        root_o = Tk()

        root_o.geometry("600x350")
        root_o.resizable(False, False)
        root_o.title("pdf-separator")

        def up_list():  # 選択したファイルを1つ前に
            indices = listbox.curselection()
            if len(indices) == 1:  # 選択した項目が１つか？
                if listbox.get(indices) == "-----------------":
                    if indices[0] > 0:
                        listbox.insert(indices[0] - 1, listbox.get(indices))
                        listbox.delete(indices[0] + 1)
                        listbox.select_set(indices[0] - 1)

        def down_list():  # 選択したファイルを1つ後に
            indices = listbox.curselection()
            if len(indices) == 1:  # 選択した項目が１つか？
                if listbox.get(indices) == "-----------------":
                    if indices[0] < listbox.size() - 1:
                        listbox.insert(indices[0] + 2, listbox.get(indices))
                        listbox.delete(indices)
                        listbox.select_set(indices[0] + 1)

        def add_line():  # 選択したファイルの1つ後に空白のページを追加
            indices = listbox.curselection()
            if len(indices) == 1:  # 選択した項目が１つか？
                listbox.insert(indices[0] + 1, "-----------------")

        def delete_line():  # 選択したファイルの1つ後に空白のページを追加
            indices = listbox.curselection()
            if len(indices) == 1:  # 選択した項目が１つか？
                if listbox.get(indices) == "-----------------":
                    listbox.delete(indices[0])

        def btn_click_ok():
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
                pdf_file_name = name + "-" + str(file_num + 1) + ".pdf"
                pdf_file_writer = PdfWriter()
                with open(pdf_file_name, "wb") as file:
                    for page_num in file_contents:
                        file_object = pdf_file_reader.pages[page_num]
                        pdf_file_writer.add_page(file_object)
                    pdf_file_writer.write(file)  # openしたファイルに書き込む
                    # with構文によりプログラムの終了時に自動的に閉じられる
                file_num = file_num + 1

            pdf_file_writer.close()  # writerを閉じる
            messagebox.showinfo("pdf-separator", "処理が完了しました。")

            root_o.quit()
            root_o.destroy()
            sys.exit()

        def click_close():
            messagebox.showinfo(
                "pdf-separator",
                "キャンセルされました。\n最初からやり直してください。",
            )
            root_o.destroy()
            root.destroy()
            sys.exit()

        # フレームの生成
        frame = Frame(root_o)
        frame.place(x=20, y=30)

        # Listboxウィジェットを生成し、読み込んだファイルを入れる
        listbox = Listbox(frame, width=80, height=15, selectmode="signal")
        for num in range(page_n):
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
        label.place(x=20, y=10)

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

        messagebox.showinfo("pdf-separator", "処理が完了しました。")
        root.destroy()

    return
