# Standard Library
import sys

# Third Party Library
from merger_func import checking, files_reading, merging, option

files_read = files_reading()
files_read = checking(files_read=files_read)
file_name_save = merging(files_read=files_read)
option(files_read=files_read, file_name_save=file_name_save)
sys.exit()
