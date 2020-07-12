# ex UA_det, gt 생성기 (gt는 추가 작업 필요)
import os

cnt_p=0

base_dir = os.getcwd() # 기본 경로

in_dir_img = os.path.join(base_dir, 'imglist\\') # input 경로 xml 파일 위치

in_dir = os.path.join(base_dir, 'input_det\\') # input 경로 xml 파일 위치
out_dir = os.path.join(base_dir, 'result_2\\') # output 경로 출력되는 txt파일 위치

raw_list = os.listdir(in_dir) # input 경로내 파일 리스트

for target in raw_list:

    name1, name2, dummy1, dummy2 = target.split('_')

    name = name1 + '_' + name2

    target_dir = os.path.join(out_dir, name + '\\det\\')

    if not(os.path.isdir(target_dir)): # 시퀸스별 저장 경로 생성
        os.makedirs(target_dir)

    wrt = open(target_dir + 'det' + '.txt', 'w') # 파일 쓰기

    rd = open(in_dir + target, mode='rt') # 읽을 대상
    
    line = rd.readline() # 시작 줄 읽기
    
    # 한줄씩 읽기 시작 및 찾아 바꾸기, 파일내 줄이 없을 때까지 (None)
    while line:

        frame, id, xmin, ymin, width, height, conf = line.split(',')

        conf = conf.replace('\n','')

        id = '-1'
        
        final = frame + ',' + '-1' + ',' + xmin + ',' + ymin + ',' + width + ',' + height + ',' + conf + ',-1,-1,-1\n' # frame,-1,box,box,box,box,conf,-1,-1,-1  // frame,id,box,box,box,box,conf
        
        wrt.write(final) # 한줄 쓰기

        del line # 버퍼 지우기

        line = rd.readline() 
    # 끝

    rd.close() # 다음 파일 읽기 준비

    wrt.close() # 다음 파일 쓰기 준비

    cnt_p += 1 # 디버깅용 처리된 파일 수

    print(cnt_p) # 디버깅용
