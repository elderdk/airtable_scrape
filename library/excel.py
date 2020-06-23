from openpyxl import Workbook
import os

def make_file(path, filename):
    fname = os.path.join(path, filename)
    if os.path.isfile(fname):
        return fname
    else:
        wb = Workbook()
        wb.save(fname)
    
    return fname