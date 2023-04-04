import os, sys
import re
from tkinter import messagebox, filedialog, Tk
from pypdf import PdfWriter

dirname = os.path.dirname(__file__) 
iDir = os.path.abspath(dirname) 
root = Tk()
root.withdraw()

def files_reading():
    """
    ファイルの読み込み
    読み込まれたファイルのリストを返す
    """
    files_read = filedialog.askopenfilenames(
        title='開く',
        filetypes=[("PDF file","*.pdf")], 
        initialdir=iDir)

    return files_read

def checking(files_read):
    """
    読み込んだファイルのリストの結合前処理（存在の確認や並べ替えなど）
    処理後のリストを返す
    * 状況によりmergingに行かずにchecking段階で処理を終わらせる
    """
    files_found = ''
    for file_name in files_read:
        files_found = files_found + file_name + '\n'
    
    if files_read != '': # ファイルが存在する場合        
        yes_no = messagebox.askquestion('Pdf-merger', '現在の状態では以下の' + str(len(files_read)) + 
                                        '個のファイルが以下の順番で結合されます：\n' + files_found + 
                                        '\n逆順に並べ替えますか?')

        if yes_no == 'yes':
            files_read = list(reversed(files_read))
        else:
            files_read = files_read
        
        files_found = ''
        for file_name in files_read:
            files_found = files_found + file_name + '\n'

        ok = messagebox.askokcancel(
            'Pdf-merger', '以下の' + str(len(files_read)) + '個のファイルを以下の順番で結合します：\n' + 
            files_found + '\nよろしければ、OKを押してください。')

        if ok:
            return files_read
        
        else:
            messagebox.showinfo('Pdf-merger', 'キャンセルされました。\n最初からやり直してください。')
            root.destroy()
            sys.exit()
    
    else:
        messagebox.showerror('Pdf-merger', 'データが選択されていません。\n最初からやり直してください。')
        root.destroy()
        sys.exit()

def merging(files_read):
    """
    結合の本体
    """
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
    return
        
