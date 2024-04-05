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
    filedialog,
    messagebox,
)

# First Party Library
from compressor import compressing

# Third Party Library
from pypdf import PdfWriter
from send2trash import send2trash

ctypes.windll.shcore.SetProcessDpiAwareness(1)

dirname = os.path.dirname(__file__)
iDir = os.path.abspath(dirname)
root = Tk()
root.withdraw()


def merging(files_read: list[str]) -> None:
    """
    結合の本体
    """
    root_o = Tk()

    root_o.geometry("600x350")
    root_o.resizable(False, False)
    root_o.title("pdf-merger")

    def up_list() -> None:  # 選択したファイルを1つ前に
        indices = listbox.curselection()
        if len(indices) == 1:  # 選択した項目が１つか？
            if indices[0] > 0:
                listbox.insert(indices[0] - 1, listbox.get(indices))
                listbox.delete(indices[0] + 1)
                listbox.select_set(indices[0] - 1)

    def down_list() -> None:  # 選択したファイルを1つ後に
        indices = listbox.curselection()
        if len(indices) == 1:  # 選択した項目が１つか？
            if indices[0] < listbox.size() - 1:
                listbox.insert(indices[0] + 2, listbox.get(indices))
                listbox.delete(indices)
                listbox.select_set(indices[0] + 1)

    def add_page() -> None:  # 選択したファイルの1つ後に空白のページを追加
        indices = listbox.curselection()
        if len(indices) == 1:  # 選択した項目が１つか？
            listbox.insert(indices[0] + 1, "（空白のページ）")

    def delete_page() -> None:  # 選択したファイルの1つ後に空白のページを追加
        indices = listbox.curselection()
        if len(indices) == 1:  # 選択した項目が１つか？
            if listbox.get(indices) == "（空白のページ）":
                listbox.delete(indices[0])

    def btn_click_ok() -> None:
        pdf_file_merger = PdfWriter()
        insert_page_n = 0

        # 出だしから空白のページが連続しているとき、他の結合後に改めて
        # insertするので、予め枚数を計算しておく
        for i in range(listbox.size()):
            if listbox.get(0) == "（空白のページ）":
                if listbox.get(i) != "（空白のページ）":
                    break
                insert_page_n = insert_page_n + 1

        # 結合本体。先頭から連続していない空白のページを見つけたら、
        # すぐに追加し、他のPDFは順当にappend。
        for i in range(listbox.size()):
            if listbox.get(i) == "（空白のページ）":
                if i > insert_page_n:
                    pdf_file_merger.add_blank_page()
            else:
                pdf_file_merger.append(listbox.get(i))

        # 出だしから連続している空白のページを最後にまとめて追加。
        for i in range(insert_page_n):
            pdf_file_merger.insert_blank_page(index=i - i)

        pdf_name_save = filedialog.asksaveasfilename(
            title="結合したファイルを名前を付けて保存",
            filetypes=[("PDF file", "*.pdf")],
            initialdir=iDir,
        )

        if pdf_name_save.rfind(".pdf") == -1:
            pdf_name_save = pdf_name_save + ".pdf"
            # 右から検索して.pdfが無かったら勝手に付け足す

        with open(pdf_name_save, "wb") as file:
            pdf_file_merger.write(file)
        pdf_file_merger.close()  # writer を閉じる

        # 結合後のオプション機能
        delete = messagebox.askquestion(
            "pdf-merger",
            "結合に使用したPDFをゴミ箱に移動しますか？",
        )

        if delete == "yes":
            for pdf_name in files_read:
                # 上書きの場合は本体を削除しない
                if pdf_name != pdf_name_save:
                    # send2trashで使われるget_short_path_name関数の仕様で置換
                    pdf_name_delete = pdf_name.replace("/", "\\")
                    send2trash(pdf_name_delete)

        compress = messagebox.askquestion(
            "pdf-merger",
            "結合後のPDFを圧縮しますか？\n（pdf-compressorを起動します。GhostScriptが必要）",
        )

        if compress == "yes":
            compressing(pdf_name_save)

        messagebox.showinfo("pdf-merger", "処理が完了しました。")

        root_o.quit()
        root_o.destroy()
        root.quit()
        root.destroy()

    def click_close() -> None:
        messagebox.showinfo(
            "pdf-merger",
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
    for pdf_name in files_read:
        listbox.insert(END, pdf_name)
    listbox.pack(fill="x", side="left")

    # スクロールバーの生成
    scroll = Scrollbar(frame, orient="vertical")
    listbox.configure(yscrollcommand=scroll.set)
    scroll.config(command=listbox.yview)
    scroll.pack(side="right", fill="y")

    # ラベルの配置
    label = Label(
        root_o,
        text="PDFの結合順を設定してください（上から順に結合します）。",
    )
    label.pack()
    label.place(x=20, y=3)

    # ボタンを定義して配置
    button_add_page = Button(
        root_o, text="空白のﾍﾟｰｼﾞを追加", command=add_page
    )
    button_delete_page = Button(
        root_o, text="空白のﾍﾟｰｼﾞを削除", command=delete_page
    )
    button_ok = Button(root_o, text="結合", command=btn_click_ok)
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
