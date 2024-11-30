# File Room Guy

import os, shutil
path = r"D:/projects/file_sorter/file-room-guy/junk/"
filename = os.listdir(path)
categories = ['images', 'archives', 'exe files', 'docx files', 'pdf files', 'xlsx files', 'txt files']

for i in range(0, len(categories)):
    if not os.path.exists(path + categories[i]):
        os.makedirs(path + categories[i])

for file in filename:
    if '.png' in file and not os.path.exists(path + "images/" + file):
        shutil.move(path + file, path + "images/" + file)
    elif '.jpg' in file and not os.path.exists(path + "images/" + file):
        shutil.move(path + file, path + "images/" + file)
    elif '.docx' in file and not os.path.exists(path + "docx files/" + file):
        shutil.move(path + file, path + "docx files/" + file)
    elif '.txt' in file and not os.path.exists(path + "txt files/" + file):
        shutil.move(path + file, path + "txt files/" + file)
    elif '.xlsx' in file and not os.path.exists(path + "xlsx files/" + file):
        shutil.move(path + file, path + "xlsx files/" + file)
    elif '.pdf' in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif '.exe' in file and not os.path.exists(path + "exe files/" + file):
        shutil.move(path + file, path + "exe files/" + file)
    elif '.zip' in file and not os.path.exists(path + "archives/" + file):
        shutil.move(path + file, path + "archives/" + file)
    elif '.7z' in file and not os.path.exists(path + "archives/" + file):
        shutil.move(path + file, path + "archives/" + file)
    elif '.rar' in file and not os.path.exists(path + "archives/" + file):
        shutil.move(path + file, path + "archives/" + file)
       