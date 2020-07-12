# 4. 한곳에 모은 파일들 세가지 클래스로 나누기(Annotation만)

import os
import shutil

base_dir = 'D:\Visual Studio Solution\DETRAC_processed'
in_dir = os.path.join(base_dir, '3_class_joint\\test\\test_annotation\\') # input 경로
out_dir = os.path.join(base_dir, '3_class_seperated\\') # output 경로

car_dir = os.path.join(out_dir, 'car\\test_annotation\\')
bus_dir = os.path.join(out_dir, 'bus\\test_annotation\\')
van_dir = os.path.join(out_dir, 'van\\test_annotation\\')

raw_list = os.listdir(in_dir) # input 경로내 파일 리스트

num = 0

for list in raw_list:
    file = os.path.join(in_dir + list)
    rd = open(file, mode='rt')
    line = rd.readline()

    car_opened = 0
    bus_opened = 0
    van_opened = 0

    print(list)
    while line:
        name, ext = list.split('.')

        detection_car = line.find('car')
        detection_bus = line.find('bus')
        detection_van = line.find('van')
    
        if detection_car == 0:
            if car_opened == 1:
                car_wrt.write(line)
            else:
                car_wrt = open(car_dir + name + '.' + ext, mode='wt')
                car_wrt.write(line)
                car_opened = 1
            
        elif detection_van == 0:
            if van_opened == 1:
                van_wrt.write(line)
            else:
                van_wrt = open(van_dir + name + '.' + ext, mode='wt')
                van_wrt.write(line)
                van_opened = 1

        elif detection_bus == 0:
            if bus_opened == 1:
                bus_wrt.write(line)
            else:
                bus_wrt = open(bus_dir + name + '.' + ext, mode='wt')
                bus_wrt.write(line)
                bus_opened = 1

        del line
        line = rd.readline()

    try:
        car_wrt.close()
        van_wrt.close()
        bus_wrt.close()
    except:
        pass


    

                
