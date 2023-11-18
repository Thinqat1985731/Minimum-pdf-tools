# Standard Library
import sys
from tkinter import Button, Label, Radiobutton, StringVar, Tk

# First Party Library
from common_func import checking, files_reading
from compressor_func import compressing
from merger_func import merging, option
from separator_func import separating

root = Tk()
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


label = Label(root, text="ツールを選択してください")
label.pack()
label.place(x=20, y=10)

button = Button(root, text="OK", command=btn_click)
button.place(x=20, y=180)

root.mainloop()

files_read = files_reading()
filse_read = checking(files_read=files_read, program=radio_var.get())

if radio_var.get() == "pdf-merger":
    file_name_save = merging(files_read=files_read)
    option(files_read=files_read, file_name_save=file_name_save)
elif radio_var.get() == "pdf-separator":
    separating(files_read=files_read)
elif radio_var.get() == "pdf-compressor":
    compressing(files_read=files_read)
sys.exit()
