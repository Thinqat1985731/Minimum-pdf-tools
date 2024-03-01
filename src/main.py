# Standard Library
import sys
from tkinter import Button, Label, Radiobutton, StringVar, Tk

# First Party Library
from compressor import compressing
from merger import merging
from preprocessor import dataloader, startcheck
from separator import separating

root = Tk()

root.geometry("250x240")
root.resizable(False, False)
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


def btn_click() -> None:
    root.quit()
    root.destroy()


def click_close() -> None:
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

files_read = dataloader(tool=radio_var.get())
startcheck(tool=radio_var.get(), files_read=files_read)

if tool == "pdf-merger":
    merging(files_read=files_read)
    sys.exit()
elif tool == "pdf-separator":
    separating(file_read=files_read)
    sys.exit()
else:
    compressing(file_read=files_read)
    sys.exit()
