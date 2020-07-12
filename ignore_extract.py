# ext ignore region 찾기
import os

line_num = 0 # 줄 세기
avb_cnt = 0 # 유효 파일 수 세기
cnt = 0 # 총 파일 수 세기
cnt_p = 0 # 작업한 파일 수
igr = 0 # ignored region 무시
brace_list = [0 for _ in range(10)]
num = 'ignore' # num 초기화
others_num = 0 # 디버깅용
obj_num = 0
num_car = 0
num_bus = 0
num_van = 0 # 디버깅용

frame_car = 0 # 디버깅용
frame_bus = 0
frame_van = 0
frame_others = 0 # 디버깅용

base_dir = os.getcwd() # 기본 경로
in_dir = os.path.join(base_dir, 'input\\') # input 경로 xml 파일 위치
out_dir = os.path.join(base_dir, 'result\\') # output 경로 출력되는 txt파일 위치
raw_list = os.listdir(in_dir) # input 경로내 파일 리스트

car_out_dir = os.path.join(out_dir, 'car\\')
van_out_dir = os.path.join(out_dir, 'van\\')
bus_out_dir = os.path.join(out_dir, 'bus\\')


def finder(): # 큰따옴표 내부 주소 특정 및 추출

    for i in range(10):
        brace_list[i] = 0

    i = 0
    index = -1
    while True:
        index = line.find('"', index + 1)
        if index == -1:
            break
        elif index != brace_list[i]:
            brace_list[i] = index
            i += 1
        else:
            pass
    return None

   
# 파일 유무 확인
if not raw_list:
    print("There is no file to excute.")
    exit()


# input 폴더에 존재하는 파일 수 만큼 반복
for target in raw_list:
    ini = 0 # 이니시에이팅

    name, ext = target.split('.') # 파일 이름과 확장자 분리

    #seperate_destination = (os.path.join(out_dir, name) + '\\') # 시퀸스별로 저장시 경로 설정

    #if not(os.path.isdir(seperate_destination)): # 시퀸스별 저장 경로 생성
        #os.makedirs(seperate_destination)

    # wrt = open(seperate_destination + 'ignore' + name + '.txt', 'w') # 파일 쓰기

    wrt = open(out_dir + 'ignore_' + name + '.txt', 'w') # 파일 쓰기
    appear_bus = 0 # 디버깅용
    appear_car = 0 
    appear_van = 0
    appear_others = 0 # 디버깅용

    rd = open(in_dir + target, mode='rt') # 읽을 대상
    
    line = rd.readline() # 시작 줄 읽기
    
    # 한줄씩 읽기 시작 및 찾아 바꾸기, 파일내 줄이 없을 때까지 (None)
    while line:
        ignore_target = line.find('ignored_region') # ignore 감지
        ignore_noval = line.find('ignored_region/') # ignore exception
        stop_igr_target = line.find('/ignored_region') # ignore 종료 감지

        ex_target = line.find('box') # 좌표 감지

        if ignore_target > 0:# ignore 구역이 있다면 넘어가기
            if ignore_noval > 0:# ignore 반대 슬레시는 예외
                pass
            else:
                igr = 1

        if stop_igr_target > 0: # ignore 종료가 나올때 까지 작업 중지
            igr = 0


        elif ex_target > 0 and igr == 1: # bounding box 좌표 특정

            finder()

            bh_st = brace_list[0]
            bh_ed = brace_list[1]

            wd_st = brace_list[2]
            wd_ed = brace_list[3]

            tp_st = brace_list[4]
            tp_ed = brace_list[5]

            lf_st = brace_list[6]
            lf_ed = brace_list[7]

            bx = str(round(float(line[bh_st + 1:bh_ed])))  # left
            wd = str(round(float(line[wd_st + 1:wd_ed])))  # top
            tp = str(round(float(line[tp_st + 1:tp_ed]))) # width
            lf = str(round(float(line[lf_st + 1:lf_ed]))) # height

            flt_bx = float(bx)
            flt_wd = float(wd)
            flt_tp = float(tp)
            flt_lf = float(lf)

            Xmax = str(round(flt_bx + flt_tp)) # left + width
            Ymax = str(round(flt_wd + flt_lf)) # top + height

            if float(Xmax) > 960: # 해상도를 초과하는 박스 크기 축소
                Xmax = '960'
            if float(Ymax) > 540:
                Ymax = '540'

            box = bx + ',' + wd + ',' + tp + ',' + lf # xmin, ymin, width, height
            #box = bx + ',' + wd + ',' + Xmax + ',' + Ymax + ',' # min, max
       
            final = box +'\n'

            #if ini == 0: # 디버깅용
            #    wrt.write('frame,id,xmin,ymin,width,height,att_1,att_2,att_3\n')
            #    ini = 1

            wrt.write(final) # 한줄 쓰기

        del line # 버퍼 지우기

        line = rd.readline() 
    # 끝

    rd.close() # 다음 파일 읽기 준비

    wrt.close() # 다음 파일 쓰기 준비

    cnt_p += 1 # 디버깅용 처리된 파일 수

    print(cnt_p) # 디버깅용

print("Processed files : ",cnt_p)

re_dir = os.listdir(out_dir) # input 경로내 파일 리스트

