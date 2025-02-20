# Standard Library
import ctypes
import sys
from tkinter import Button, Label, Radiobutton, StringVar, Tk

# First Party Library
from common import dataloader, startchecker, timezonesetter
from compressor import compressing
from merger import merging
from separator import separating

if __name__ == "__main__":
    # ツール選択
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root = Tk()

    root.geometry("250x240")
    root.resizable(False, False)
    root.title("minimum-pdf-tools")

    radio_var = StringVar(root)

    radio1 = Radiobutton(
        root, value="pdf-merger", variable=radio_var, text="pdf-merger"
    )
    radio1.pack()
    radio1.place(x=20, y=75)

    radio2 = Radiobutton(
        root, value="pdf-separator", variable=radio_var, text="pdf-separator"
    )
    radio2.pack()
    radio2.place(x=20, y=100)

    radio3 = Radiobutton(
        root, value="pdf-compressor", variable=radio_var, text="pdf-compressor"
    )
    radio3.pack()
    radio3.place(x=20, y=125)

    radio_var.set("pdf-merger")

    def btn_click() -> None:
        root.quit()
        root.destroy()

    def click_close() -> None:
        root.quit()
        root.destroy()
        sys.exit()

    label = Label(root, text="ツールを選択してください")
    label.pack()
    label.place(x=20, y=10)

    button = Button(root, text="OK", command=btn_click)
    button.place(x=125, y=180, width=100)

    root.protocol("WM_DELETE_WINDOW", click_close)
    root.mainloop()
    tool = radio_var.get()

    # タイムゾーン選択
    tzinfo = timezonesetter()

    # 処理開始の確認
    files_read = dataloader(tool=radio_var.get())
    startchecker(tool=radio_var.get(), files_read=files_read)

    # 実際の処理
    if tool == "pdf-merger":
        merging(files_read=files_read, tzinfo=tzinfo)
        sys.exit()
    elif tool == "pdf-separator":
        separating(file_read=files_read, tzinfo=tzinfo)
        sys.exit()
    else:
        compressing(file_read=files_read, tzinfo=tzinfo)
        sys.exit()
