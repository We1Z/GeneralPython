import os

file_Path = 'C:/users/weiwe/Downloads/TestFile.txt'

print(file_Path)
if os.path.isfile(file_Path):
    os.remove(file_Path)
    print("File has been removed")

else:
    print("File doesnt not exists")