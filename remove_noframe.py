# 2. annotation이 없는 프레임 삭제

import shutil
import os

base_dir = os.getcwd()
in_dir = os.path.join(base_dir, 'imglist\\') # input 경로
out_dir = os.path.join(base_dir, 'img_result\\') # output 경로
folder_list = os.listdir(in_dir) # 폴더 리스트
num = 0
c_num = 0
d_num = 0

check_dir = os.path.join(base_dir, 'result\\')
check_folder = os.listdir(check_dir) # 폴더 리스트

print("Total folders : ", len(folder_list))
wrt = open(base_dir + '\\debug.txt', mode='wt')

for target in folder_list:
    for checks in check_folder:
        if target == checks:
            c_num += 1
            print('checks', c_num)
            break
        else:
            pass


for i in range(0, c_num):

    target = folder_list[i]
    check_f = check_folder[i]

    out_folder = os.path.join(out_dir, target) + '\\'

    if not(os.path.isdir(out_folder)):
        os.makedirs(out_folder)

    img_loca = os.path.join(in_dir, target + '\\')
    img_list = os.listdir(img_loca)
    check_list = os.listdir(check_dir + check_f + '\\')

    for img_name in img_list:
        name, ext = img_name.split('.')
        debug = 1
        for check in check_list:
            c_name, c_ext = check.split('.')
            if name == c_name:
                num += 1
                target_img_dir = os.path.join(img_loca, name + '.jpg')
                shutil.copy(target_img_dir, out_folder + c_name + '.jpg')
                debug = 0
                break

            elif name != c_name:
                pass

        if debug == 1:
            print("뭐시여 없네?", img_name)
            d_num += 1
            wrt.write(target + " // " + img_name + '\n')
        else:
            pass
        

wrt.write('total missing : ' + str(d_num) + '\n')
wrt.close()






                