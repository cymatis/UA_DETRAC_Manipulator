# seq info 생성기
import os

base_dir = os.getcwd() # 기본 경로
in_dir = os.path.join(base_dir, 'imglist\\') # input 경로 xml 파일 위치
out_dir = os.path.join(base_dir, 'result_2\\') # output 경로 출력되는 txt파일 위치
raw_list = os.listdir(in_dir) # input 경로내 파일 리스트

for target in raw_list:
    img_list = os.listdir(os.path.join((in_dir), target))
    target_dir = os.path.join(out_dir, target)
    print(target_dir)

    if not(os.path.isdir(target_dir)): # 시퀸스별 저장 경로 생성
        os.makedirs(target_dir)

    wrt = open(target_dir + '\\seqinfo' + '.ini', 'w') # 파일 쓰기

    wrt.write('[Sequence]\n')
    wrt.write('name=' + target + '\n')
    wrt.write('imDir=img1\n')
    wrt.write('frameRate=30\n')
    wrt.write('seqLength=' + str(len(img_list)) + '\n')
    wrt.write('imWidth=960\n')
    wrt.write('imHeight=540\n')
    wrt.write('imExt=.jpg\n')

    wrt.close()
