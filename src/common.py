# Standard Library
import ctypes
import os
import sys
import zoneinfo
from datetime import datetime
from tkinter import (
    BooleanVar,
    Button,
    Checkbutton,
    Label,
    StringVar,
    Tk,
    filedialog,
    messagebox,
    ttk,
)
from zoneinfo import ZoneInfo

dirname = os.path.dirname(__file__)
initial_dir = os.path.abspath(dirname)


def timezonesetter() -> list[ZoneInfo, int]:
    """
    タイムゾーンの設定
    """
    root_z = Tk()

    root_z.geometry("250x240")
    root_z.resizable(False, False)
    root_z.title("pdf-compressor")

    available_timezones_list = list(zoneinfo.available_timezones())
    available_timezones_list.sort()
    string_var = StringVar(root_z)
    boolean_var = BooleanVar(root_z)
    boolean_var.set(False)

    combobox = ttk.Combobox(
        root_z,
        height=10,
        width=20,
        state="readonly",
        textvariable=string_var,
        values=available_timezones_list,
    )
    combobox.pack()
    combobox.place(x=20, y=75)

    check = Checkbutton(
        root_z, variable=boolean_var, text="サマータイムを考慮"
    )
    check.pack()
    check.place(x=20, y=125)

    def btn_click() -> int:
        root_z.quit()
        root_z.destroy()

    def click_close() -> None:
        messagebox.showinfo(
            "pdf-compressor",
            "キャンセルされました。\n最初からやり直してください。",
        )
        root_z.quit()
        root_z.destroy()
        sys.exit()

    label = Label(root_z, text="タイムゾーンを選んでください。")
    label.pack()
    label.place(x=20, y=10)

    button = Button(root_z, text="OK", command=btn_click)
    button.place(x=125, y=180, width=100)

    root_z.protocol("WM_DELETE_WINDOW", click_close)
    root_z.mainloop()

    fold = 0 if boolean_var else 1
    if string_var == "":
        return
    else:
        return [ZoneInfo(string_var.get()), fold]


def dataloader(tool: str) -> list[str] | str:
    """
    PDFデータの読み込み
    """
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    if tool == "pdf-merger":
        # 複数PDFファイルを開く
        files_read = filedialog.askopenfilenames(
            title="開く",
            filetypes=[("PDF file", "*.pdf")],
            initialdir=initial_dir,
        )
    else:
        # 単一PDFファイルを開く
        files_read = filedialog.askopenfilename(
            title="開く",
            filetypes=[("PDF file", "*.pdf")],
            initialdir=initial_dir,
        )
    return files_read


def startchecker(tool: str, files_read: list[str] | str) -> None:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    if files_read != "":  # ファイルが存在する場合
        files_found = ""
        for file_name in files_read:
            files_found = files_found + file_name + "\n"

        if tool == "pdf-merger":
            ok = messagebox.askokcancel(
                tool,
                "以下の"
                + str(len(files_read))
                + "個のファイルを結合します：\n"
                + files_found
                + "\nよろしければ、OKを押してください"
                + "\n（OKを押すと、結合順の設定に移行します）。",
            )
        elif tool == "pdf-separator":
            ok = messagebox.askokcancel(
                tool,
                "以下のファイルを分割します：\n"
                + files_read
                + "\nよろしければ、OKを押してください。",
            )
        else:
            ok = messagebox.askokcancel(
                tool,
                "以下のファイルを圧縮します：\n"
                + files_read
                + "\nよろしければ、OKを押してください。",
            )

        if ok:
            return
        else:
            messagebox.showinfo(
                tool,
                "キャンセルされました。\n最初からやり直してください。",
            )
            sys.exit()

    else:
        messagebox.showerror(
            tool,
            "データが選択されていません。\n最初からやり直してください。",
        )
        sys.exit()


def metamaker(
    tzinfo: list[ZoneInfo, int], old_meta: dict[str, str] | None = None
) -> dict[str, str]:
    time = datetime.now(tz=tzinfo[0]).strftime("D\072%Y%m%d%H%M%S")
    if tzinfo[1] == 1:  # foldの使用が設定されていた場合は適用
        time.replace(fold=1)
    if old_meta is None:
        # 新規のメタデータであるpdf_mergerについて、処理時の日時のみ追加
        meta = {
            "/CreationDate": time,
            "/ModDate": time,
        }
    else:
        # 既存メタデータを使用するpdf_separatorとpdf_compressorについて、
        # PDFの更新としてCreationDateは保持してModDateに処理時の日時を融合
        meta = {
            **old_meta,
            **{
                "/ModDate": time,
            },
        }
    return meta
