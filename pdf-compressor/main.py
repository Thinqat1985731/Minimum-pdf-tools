import sys
from compressor_func import files_reading, checking, compressing

files_read = files_reading()
filse_read = checking(files_read=files_read)
compressing(files_read=files_read)
sys.exit()
