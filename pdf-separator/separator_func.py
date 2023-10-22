import os, sys
import re
from tkinter import messagebox, filedialog, Tk
from pypdf import PdfReader, PdfWriter

root = Tk()
root.withdraw()

def files_reading():
    """
    ファイルの読み込み
    読み込まれたファイルのリストを返す
    """
    dirname = os.path.dirname(__file__) 
    iDir = os.path.abspath(dirname) 
    files_read = filedialog.askopenfilenames(
        title='開く',
        filetypes=[("PDF file","*.pdf")], 
        initialdir=iDir)

    return files_read

def checking(files_read):
    """
    読み込んだファイルのリストの結合前処理（存在の確認や並べ替えなど）
    処理後のリストを返す
    * 状況によりseparatingに行かずにchecking段階で処理を終わらせる
    """
    files_found = ''

    for file_name in files_read:
        files_found = files_found + file_name + '\n'
    
    if files_found != '': # ファイルが存在する場合       
        ok = messagebox.askokcancel(
            'Pdf-separator', '以下の' + str(len(files_read)) + 
            '個のファイルを個々のページに分割します：\n' + files_found)

        if ok:
            return
        
        else:
            messagebox.showinfo('Pdf-merger', 'キャンセルされました。\n最初からやり直してください。')
            root.destroy()
            sys.exit()
    
    else:
        messagebox.showerror('Pdf-merger', 'データが選択されていません。\n最初からやり直してください。')
        root.destroy()
        sys.exit()

def separating(files_read):
    """
    分離の本体
    """
    for file_name in files_read:
            (name, extention) = os.path.splitext(file_name)  # 拡張子を分離
            pdf_file_reader = PdfReader(file_name)
            page_n =  len(pdf_file_reader.pages)  # ページ数を取得

            for num in range(page_n):
                file_object = pdf_file_reader.pages[num]  # 指定ページの内容だけ抜き出す
                pdf_file_name = name + '-' + str(num + 1) + '.pdf'
                pdf_file_writer = PdfWriter()
                with open(pdf_file_name, 'wb') as file:
                    pdf_file_writer.add_page(file_object)  # 書き出したいデータを追加
                    pdf_file_writer.write(file)  # openしたファイルに書き込む
                    # with構文によりプログラムの終了時に自動的に閉じられる
                
    pdf_file_writer.close() # writerを閉じる
    
    messagebox.showinfo('Pdf-separator', '処理が完了しました。')
    root.destroy()
    return
        