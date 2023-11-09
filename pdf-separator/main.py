# Standard Library
import sys

# Third Party Library
from separator_func import checking, files_reading, separating

files_read = files_reading()
filse_read = checking(files_read=files_read)
separating(files_read=files_read)
sys.exit()
