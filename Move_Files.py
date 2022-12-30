import os
import shutil

fromDir = "C:/Projects/WhiteHat Jr/Python/File_Segregation/image_files"
toDir = "C:/Projects/WhiteHat Jr/Python/File_Segregation/image_files"

filesList = os.listdir(fromDir)

print(filesList)

for i in filesList:
    nam, ext = os.path.splitext(i)
    if (ext in [".jpg", ".png", ".gif", ".jpeg", ".pdf", ".jfif"]):
        originalFilePath = fromDir + "/" + i
        moveToFilePath = fromDir + "/" + ext
        newFilePath = fromDir + "/" + ext + "/" + i

        if (os.path.exists(moveToFilePath)):
            shutil.move(originalFilePath, newFilePath)
        else:
            os.makedirs(moveToFilePath)
            shutil.move(originalFilePath, newFilePath)
