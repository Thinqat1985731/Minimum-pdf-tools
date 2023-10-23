import sys
from compressor_func import checking, compressing, files_reading

files_read = files_reading()
filse_read = checking(files_read=files_read)
compressing(files_read=files_read)
sys.exit()
