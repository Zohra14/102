import os
import shutil
from_dir="C:/Users/rtj00/OneDrive/Desktop/python class/test"
to_dir="C:/Users/rtj00/OneDrive/Desktop/python class/"
list_of_files=os.listdir(from_dir)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    if extension=='':
        continue
    if extension in [".gif",".png",".jpg"]:
        path1=from_dir + "/" + file_name
        path2=to_dir + "/" + "img_files"
        path3=to_dir + "/" + "img_files" + "/" + file_name
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
