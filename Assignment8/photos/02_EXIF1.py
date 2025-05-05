'''
Python Image Library Basics
Extracting EXIF Data from a JPEG
CYBV 312 Spring 2025
'''

import sys

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

#Extract Basic EXIF Data
print(f"\nExtract JPEG EXIF Data\n")
imageFileName = input("Enter JPEG: ")


try:
    pilImage = Image.open(imageFileName)
    exifData = pilImage._getexif()
    
except Exception as err:
    sys.exit(f"\nPIL Exception {err}")
    
if not exifData:
    sys.exit(f"\nNo EXIF data\n")
    
#Process eathTag
for tag, theValue in exifData.items():
    tagValue = TAGS.get(tag, tag)
    tagData = exifData.get(tag)
    
    if tagValue != "GPSInfo":
        #Display the Basic Tag Data
        print("="*40)
        print(f"TAG:\t{tagValue}")
        print(f"DATA:\t{tagData}")
        
    else:
        print("GPS Data Found")
        #Process GPS Data
        for tag in theValue:     
            gpsTag = GPSTAGS.get(tag, tag)
            print(f"\t{gpsTag} {theValue[tag]}")         
           