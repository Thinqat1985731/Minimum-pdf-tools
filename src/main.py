# Standard Library
import os
import sys
from tkinter import (
    Button,
    Label,
    Radiobutton,
    StringVar,
    Tk,
    filedialog,
)

# First Party Library
from compressor_func import compressing, compressor_check
from merger_func import merger_check, merging
from separator_func import separating, separator_check

root = Tk()
dirname = os.path.dirname(__file__)
iDir = os.path.abspath(dirname)
root.geometry("250x240")
root.title("minimum-pdf-tools")

radio_var = StringVar(root)

radio1 = Radiobutton(
    root, value="pdf-merger", variable=radio_var, text="pdf-merger"
)
radio1.pack()
radio1.place(x=20, y=82)

radio2 = Radiobutton(
    root, value="pdf-separator", variable=radio_var, text="pdf-separator"
)
radio2.pack()
radio2.place(x=20, y=104)

radio3 = Radiobutton(
    root, value="pdf-compressor", variable=radio_var, text="pdf-compressor"
)
radio3.pack()
radio3.place(x=20, y=126)

radio_var.set("pdf-merger")


def btn_click():
    root.quit()
    root.destroy()


def click_close():
    root.destroy()
    sys.exit()


label = Label(root, text="ツールを選択してください")
label.pack()
label.place(x=20, y=10)

button = Button(root, text="OK", command=btn_click)
button.place(x=125, y=180, width=100)

root.protocol("WM_DELETE_WINDOW", click_close)
root.mainloop()

files_read = filedialog.askopenfilenames(
    title="開く", filetypes=[("PDF file", "*.pdf")], initialdir=iDir
)

if radio_var.get() == "pdf-merger":
    files_read = merger_check(files_read=files_read)
    merging(files_read=files_read)
elif radio_var.get() == "pdf-separator":
    files_read = separator_check(files_read=files_read)
    separating(files_read=files_read)
elif radio_var.get() == "pdf-compressor":
    files_read = compressor_check(files_read=files_read)
    compressing(files_read=files_read)
sys.exit()
