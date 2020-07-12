# 3. 한곳으로 모으기

import os
import shutil

base_dir = 'C:/Users/sonic/data/'
in_dir = os.path.join(base_dir, 'img/')
out_dir = 'C:/Users/sonic/Desktop/data/img/train/'

folder_path = 'C:/Users/sonic/Desktop/data/img/train/'
file_list = os.listdir(folder_path)

num = 0
    
for files in file_list:
    name, ext = files.split('.')
    num += 1
    rename = str(num).zfill(6)
    file_path = os.path.join(folder_path, files)
    shutil.copy(file_path, out_dir + rename + '.' + ext)


