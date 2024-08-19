import os
import shutil

file_need_to_organize = 'E:/MS Office Word 2007 v1014 (English) + Addintools [RH]/US'

file_type_folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi']
    }

files = os.listdir(file_need_to_organize)


for file in files:

    if os.path.isdir(os.path.join(file_need_to_organize, file)):
        continue


    file_extension = os.path.splitext(file)[1].lower()

    moved = False
    for folder, extensions in file_type_folders.items():
        if file_extension in extensions:
            folder_path = os.path.join(file_need_to_organize, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(os.path.join(file_need_to_organize, file), os.path.join(folder_path, file))
            print(f'Moved: {file} to {folder}')
            moved = True
            break

    if not moved:
        print(f'Skipped: {file} (unknown file type)')
