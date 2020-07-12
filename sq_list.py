# x. 한곳으로 모으기

import os
import shutil

base_dir = 'D:\Visual Studio Solution\DETRAC_processed\sequence'
in_dir = os.path.join(base_dir, 'Train_img\\') # input 경로
out_dir = os.path.join(base_dir, 're_Train_img\\') # output 경로


raw_list = os.listdir(in_dir) # input 경로내 파일 리스트


num = 0

wrt = open(out_dir + 'sq_list' + '.txt', 'w')

for list in raw_list:

    final = list + '\n'

    wrt.write(final)

        
    






