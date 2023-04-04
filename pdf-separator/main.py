from separator_func import files_reading, checking, separating

files_read = files_reading()
filse_read = checking(files_read=files_read)
separating(files_read=files_read)