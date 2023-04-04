from merger_func import files_reading, checking, merging

files_read = files_reading()
files_read = checking(files_read=files_read)
merging(files_read=files_read)