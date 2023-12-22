# Standard Library
import os
import subprocess
import sys
from tkinter import (
    END,
    Button,
    Frame,
    Label,
    Listbox,
    Radiobutton,
    Scrollbar,
    StringVar,
    Tk,
    filedialog,
    messagebox,
)

# Third Party Library
from pypdf import PdfWriter
from send2trash import send2trash

dirname = os.path.dirname(__file__)
iDir = os.path.abspath(dirname)
root = Tk()
root.withdraw()


def merger_check(files_read):
    """
    読み込んだファイルのリストの結合前処理（存在の確認や並べ替えなど）
    処理後のリストを返す
    * 状況によりchecking段階で処理を終わらせる
    """
    files_found = ""
    for file_name in files_read:
        files_found = files_found + file_name + "\n"

    if files_read != "":  # ファイルが存在する場合
        ok = messagebox.askokcancel(
            "pdf-merger",
            "以下の"
            + str(len(files_read))
            + "個のファイルを結合します：\n"
            + files_found
            + "\nよろしければ、OKを押してください"
            + "\n（OKを押すと、結合順の設定に移行します）。",
        )

        if ok:
            return files_read

        else:
            messagebox.showinfo(
                "pdf-merger",
                "キャンセルされました。\n最初からやり直してください。",
            )
            root.destroy()
            sys.exit()

    else:
        messagebox.showerror(
            "pdf-merger",
            "データが選択されていません。\n最初からやり直してください。",
        )
        root.destroy()
        sys.exit()


def merging(files_read):
    """
    結合の本体
    """
    root_o = Tk()
    root_o.geometry("600x350")
    root_o.title("pdf-merger")

    def up_list():  # 選択したファイルを1つ前に
        indices = listbox.curselection()
        if len(indices) == 1:  # 選択した項目が１つか？
            if indices[0] > 0:
                listbox.insert(indices[0] - 1, listbox.get(indices))
                listbox.delete(indices[0] + 1)
                listbox.select_set(indices[0] - 1)

    def down_list():  # 選択したファイルを1つ後に
        indices = listbox.curselection()
        if len(indices) == 1:  # 選択した項目が１つか？
            if indices[0] < listbox.size() - 1:
                listbox.insert(indices[0] + 2, listbox.get(indices))
                listbox.delete(indices)
                listbox.select_set(indices[0] + 1)

    def add_page():  # 選択したファイルの1つ後に空白のページを追加
        indices = listbox.curselection()
        if len(indices) == 1:  # 選択した項目が１つか？
            listbox.insert(indices[0] + 1, "（空白のページ）")

    def btn_click_ok():
        pdf_file_merger = PdfWriter()

        for i in range(listbox.size()):
            # "（空白のページ）"を見つけたら、その場で追加
            # ただし出だしが"（空白のページ）"の場合は後からinsert
            if listbox.get(i) == "（空白のページ）":
                if i != 0:
                    pdf_file_merger.add_blank_page()
            else:
                pdf_file_merger.append(listbox.get(i))

        if listbox.get(0) == "（空白のページ）":
            pdf_file_merger.insert_blank_page()

        file_name_save = filedialog.asksaveasfilename(
            title="結合したファイルを名前を付けて保存",
            filetypes=[("PDF file", "*.pdf")],
            initialdir=iDir,
        )

        if file_name_save.rfind(".pdf") == -1:
            file_name_save = file_name_save + ".pdf"
            # 右から検索して.pdfが無かったら勝手に付け足す

        pdf_file_merger.write(file_name_save)
        pdf_file_merger.close()  # writer を閉じる

        # 結合後のオプション機能
        delete = messagebox.askquestion(
            "pdf-merger",
            "結合に使用したPDFをゴミ箱に移動しますか？",
        )

        if delete == "yes":
            for file_name in files_read:
                # 上書きの場合は本体を削除しない
                if file_name != file_name_save:
                    # send2trashで使われるget_short_path_name関数の仕様で置換
                    file_name_delete = file_name.replace("/", "\\")
                    send2trash(file_name_delete)

        compress = messagebox.askquestion(
            "pdf-merger",
            "結合後のPDFを圧縮しますか？（GhostScriptが必要）",
        )

        if compress == "yes":
            root_s = Tk()
            root_s.geometry("250x240")
            root_s.title("pdf-merger")

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
                root_s.quit()
                root_s.destroy()

            label = Label(root_s, text="圧縮の設定を選んでください。")
            label.pack()
            label.place(x=20, y=10)

            button = Button(root_s, text="OK", command=btn_click)
            button.place(x=125, y=180, width=100)

            root_s.protocol("WM_DELETE_WINDOW", click_close)
            root_s.mainloop()

            file_name_temp = file_name_save.replace(".pdf", "_.pdf")
            subprocess.check_output(
                [
                    "gswin64c",
                    "-sDEVICE=pdfwrite",
                    "-dPDFSETTINGS=%s" % (radio_var.get()),
                    "-dBATCH",
                    "-dNOPAUSE",
                    "-dSAFER",
                    "-sOUTPUTFILE=%s" % (file_name_temp,),
                    file_name_save,
                ]
            )
            os.remove(file_name_save)
            os.rename(file_name_temp, file_name_save)

        messagebox.showinfo("pdf-merger", "処理が完了しました。")

        root_o.quit()
        root_o.destroy()
        sys.exit()

    def click_close():
        messagebox.showinfo(
            "pdf-merger",
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
    for file_name in files_read:
        listbox.insert(END, file_name)
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
    label.place(x=20, y=10)

    # ボタンを定義して配置
    button_add_page = Button(
        root_o, text="空白のﾍﾟｰｼﾞを追加", command=add_page
    )
    button_ok = Button(root_o, text="結合", command=btn_click_ok)
    button_up = Button(root_o, text="▲", command=up_list)
    button_down = Button(root_o, text="▼", command=down_list)

    button_add_page.place(x=305, y=300, width=150)
    button_ok.place(x=475, y=300, width=100)
    button_up.place(x=550, y=100, width=40)
    button_down.place(x=550, y=150, width=40)

    root_o.protocol("WM_DELETE_WINDOW", click_close)
    root_o.mainloop()
    return
