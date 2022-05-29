import sys

input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        p = input()
        n = int(input())
        lis = [] # 숫자가 저장될 리스트
        temp = input().split('\n')[0].split(',') # ['[1', '2', '3', '4]']
        if temp[0] != '[]':
            if len(temp) == 1: # ['[42]']
                lis.append(int(temp[0][1:-1])) # '[' ,  ']' 부분을 제외한 숫자만 append
            else:
                for i in range(len(temp)):
                    str_ = temp[i]
                    if str_ != ',':
                        if i == 0:
                            str_ = int(str_.split('[')[1])
                        elif i == len(temp)-1:
                            str_ = int(str_.split(']')[0])
                        lis.append(int(str_))
        else:
            lis = []
        # lis 입력 끝 -> [1, 2, 3, 4]
        flg = 1 # 1: 정방향, -1: 역방향
        p_idx, r_idx = 0, len(lis) - 1 # p_idx, r_idx = 정방향 idx, 역방향 idx
        for p_e in p:
            if flg == 1: # 정방향일 경우
                if p_e == 'D':
                    if p_idx > r_idx: print('error'); break
                    else: p_idx += 1
                elif p_e == 'R':
                    flg *= -1 # 뒤집기
            elif flg == -1: # 역방향일 경우
                if p_e == 'D':
                    if p_idx > r_idx: print('error'); break
                    else: r_idx -= 1
                elif p_e == 'R':
                    flg *= -1 # 뒤집기
        else: # for-else문: for문이 정상적으로 종료된 경우 else문 실행
            print('[', end='')
            if flg == 1: # 정방향
                for i in range(p_idx, r_idx+1):
                    if i == r_idx:
                        print(lis[i], end='')
                    else:
                        print(lis[i], end=',')
                print(']')
            elif flg == -1: # 역방향
                for i in range(r_idx, p_idx-1, -1):
                    if i == p_idx:
                        print(lis[i], end='')
                    else:
                        print(lis[i], end=',')
                print(']')
