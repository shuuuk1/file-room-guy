# File Room Guy

import os, shutil
path = r"D:/projects/file_sorter/file-room-guy/junk/"
filename = os.listdir(path)
categories = ['images', 'text files', 'archives', 'exe files', 'docx files', 'pdf files', 'xlsx files']

for i in range(0, len(categories)):
    if not os.path.exists(path + categories[i]):
        os.makedirs(path + categories[i])

for file in filename:
    if '.png' in file and not os.path.exists(path + "images/" + file):
        shutil.move(path + file, path + "images/" + file)
    elif '.jpg' in file and not os.path.exists(path + "images/" + file):
        shutil.move(path + file, path + "images/" + file)
