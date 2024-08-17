print("This tool is used for erasing the metadata of images in this folder - developed by ahmed almindelawy")

import os
import sys
from PIL import Image
import piexif

def metadata_erasing_function(___Target_Folder_Full_Path):
    for ___File_Name in os.listdir(___Target_Folder_Full_Path):
        if ___File_Name.lower().endswith(('.jpg', '.jpeg', '.png')):
            ___File_Path = os.path.join(___Target_Folder_Full_Path, ___File_Name)
            ___MyImage = Image.open(___File_Path)
            ___Image_Data = list(___MyImage.getdata())
            ___Image_V2 = Image.new(___MyImage.mode, ___MyImage.size)
            ___Image_V2.putdata(___Image_Data)
            ___Image_V2.save(___File_Path)

if hasattr(sys, '_MEIPASS'):
    ___Target_Folder_Full_Path = os.path.dirname(os.path.abspath(sys.executable))
else:
    ___Target_Folder_Full_Path = os.path.dirname(os.path.abspath(__file__))

metadata_erasing_function(___Target_Folder_Full_Path)

input("Press Enter to exit...")
