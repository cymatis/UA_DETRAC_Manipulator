# 5. 나누어진 Annotation에 따라 이미지도 분할

import os
import shutil

def finder(img, txt):
    img_name, img_ext = img.split('.')
    ann_name, ann_ext = txt.split('.')

    if img_name == ann_name:
        return True
    else:
        return False


base_dir = 'D:\Visual Studio Solution\DETRAC_processed\seperate'

in_car_dir = os.path.join(base_dir, 'car\\train_annotation\\') # input 경로
car_list = os.listdir(in_car_dir)
in_bus_dir = os.path.join(base_dir, 'bus\\train_annotation\\') # input 경로
bus_list = os.listdir(in_bus_dir)
in_van_dir = os.path.join(base_dir, 'van\\train_annotation\\') # input 경로
van_list = os.listdir(in_van_dir)

out_car_dir = os.path.join(base_dir, 'car\\train_image\\')
out_bus_dir = os.path.join(base_dir, 'bus\\train_image\\')
out_van_dir = os.path.join(base_dir, 'van\\train_image\\')

total_img_dir = 'D:\Visual Studio Solution\DETRAC_processed\processed\Train_img'
raw_list = os.listdir(total_img_dir) # input 경로내 파일 리스트

car_num = 0
bus_num = 0
van_num = 0

for img_list in raw_list:
    print(img_list)

    for ann_list in car_list:
        copy = finder(img_list, ann_list)

        if copy is True:
            car_num += 1
            rename = str(car_num).zfill(5)
            shutil.copy(total_img_dir + '\\' + img_list, out_car_dir + img_list)
        else:
            pass

    for ann_list in bus_list:

        copy = finder(img_list, ann_list)

        if copy is True:
            bus_num += 1
            rename = str(bus_num).zfill(5)
            shutil.copy(total_img_dir + '\\' + img_list, out_bus_dir + img_list)
        else:
            pass

    for ann_list in van_list:

        copy = finder(img_list, ann_list)

        if copy is True:
            van_num += 1
            rename = str(van_num).zfill(5)
            shutil.copy(total_img_dir + '\\' + img_list, out_van_dir + img_list)
        else:
            pass

print("car :", car_num)
print("bus :", bus_num)
print("van :", van_num)
