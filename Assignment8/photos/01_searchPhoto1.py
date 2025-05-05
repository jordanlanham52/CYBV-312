'''
Searching for Images with PIL
CYBV 312 Spring 2025 
'''

import sys
import os

from PIL import Image
from prettytable import PrettyTable

tbl=PrettyTable(['File', 'Ext', 'Format', 'Width', 'Height', 'Mode'])
DIR = "photos"
fileList = os.listdir(DIR)

for eachFile in fileList:
    path = os.path.join(DIR, eachFile)
    if os.path.isfile(path):
        ext = os.path.splitext(path)[1]
        
        try:
            with Image.open(path) as im:
                tbl.add_row([path, ext, im.format, im.size[0], im.size[1], im.mode])
                
        except Exception as err:
            tbl.add_row([path, ext, "[NA]", "[NA]", "[NA]", "[NA]"])
            pass
        
    else:
        continue
    
tbl.align = "l"
print(tbl.get_string(sortby = "Format"))