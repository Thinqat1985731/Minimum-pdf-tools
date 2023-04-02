import os
from tkinter import messagebox, filedialog, Tk
from pypdf import PdfWriter, PdfReader

dirname = os.path.dirname(__file__) 
iDir = os.path.abspath(dirname) 
root = Tk()
root.withdraw()

files_read = filedialog.askopenfilenames(
    title='開く',
    filetypes=[("PDF file","*.pdf")], 
    initialdir=iDir)

files_found = ''
for file_name in files_read:
    files_found = files_found + file_name + '\n' # 取り敢えず確認だけ取る

yes_no = messagebox.askquestion('Pdf-merger', '以下の' + str(len(files_read)) + 
                                '個のファイルを結合します：\n' + files_found + 
                                '続行しますか?')

if yes_no == 'yes':
    pdf_file_merger = PdfWriter()
    for pdf in files_read:
        pdf_file_merger.append(pdf)

    file_name_save = filedialog.asksaveasfilename(
        title='結合したファイルを名前を付けて保存',
        filetypes=[("PDF file","*.pdf")], 
        initialdir=iDir)
    if file_name_save.rfind('.pdf') == -1:
        file_name_save = file_name_save + '.pdf' 
        # 右から検索して.pdfが無かったら勝手に付け足す
    
    pdf_file_merger.write(file_name_save)
    pdf_file_merger.close() # writer を閉じる
    messagebox.showinfo('Pdf-merger', '処理が完了しました。')
    root.destroy()

else:
    messagebox.showinfo('Pdf-merger', 'キャンセルされました。\n最初からやり直してください。')
    root.destroy()