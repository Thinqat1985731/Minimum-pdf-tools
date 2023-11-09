# Standard Library
import sys

# Third Party Library
from compressor_func import checking, compressing, files_reading

files_read = files_reading()
filse_read = checking(files_read=files_read)
compressing(files_read=files_read)
sys.exit()
