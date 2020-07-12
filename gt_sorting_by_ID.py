# windows 에서 동작안함 : wb >> w 바꾸면 줄바꿈 추가 됨;;
import sys, csv ,operator

import os

base_dir = os.getcwd() # 기본 경로

in_dir = os.path.join(base_dir, 'result\\') # 
out_dir = os.path.join(base_dir, 'result_2\\') # 

raw_list = os.listdir(in_dir) # 

for target in raw_list:
    seq_dir = os.path.join(in_dir, target)
    gt_dir = os.path.join(seq_dir, 'gt')
    gt_file = os.path.join(gt_dir, 'gt.txt')

    out_seq = os.path.join(out_dir, target)
    out_gt = os.path.join(out_seq, 'gt')
    out_gt_file = os.path.join(out_gt, 'gt.txt')

    print(gt_file)

    if not(os.path.isdir(out_gt)): # 시퀸스별 저장 경로 생성
        os.makedirs(out_gt)

    reader = csv.reader(open(gt_file), delimiter=",")
    sortedlist = sorted(reader, key=lambda x: int(x[1]), reverse=False)

    with open(out_gt_file, "wb") as f:
        fileWriter = csv.writer(f, delimiter=',')
        for row in sortedlist:
            fileWriter.writerow(row)
