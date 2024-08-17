
import os
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

# You just need to change the next line by writting the path that contains the images
# that you want to delete the metadata from
___Target_Folder_Full_Path = "Path_Of_The_Folder_Contains_The_Images"

print("___ folder_path :",___Target_Folder_Full_Path)
metadata_erasing_function(___Target_Folder_Full_Path)






