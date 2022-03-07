import sys
input = sys.stdin.readline

# n번째 톱니바퀴를 d방향으로 회전시켜서 t[n]업데이트하는 함수
def spin(n, d):
    global t
    if d == -1:
        '''왼쪽(=반시계)으로 회전'''
        t_temp = t[n][0]
        t[n] = t[n][1:8] + t_temp
    elif d == 1:
        '''오른쪽(=시계)으로 회전'''
        t_temp = t[n][7]
        t[n] = t_temp + t[n][:7]

'''start of main'''
t = [[]] # 1번째 톱니바퀴를 index 1에 오게 만들기 위함
for _ in range(4):
    t.append(input().split('\n')[0]) # readline이기때문에 맨 마지막에 \n까지 읽히므로 \n부분을 제거하기 위함
# N = 0, S = 1
# 12시 방향은 t[0] to 시계방향
# 3시 방향은 t[2]
# 9시 방향은 t[6]
k = int(input())
for _ in range(k):
    t_e = [-1, -1, -1, -1, -1] # 톱니바퀴 3시방향의 값
    t_w = [-1, -1, -1, -1, -1] # 톱니바퀴 9시방향의 값
    n, d = map(int, input().split()) # 톱니바퀴 번호, 회전 방향
    t_e[n] = t[n][2] # t[n]의 3시방향의 값
    t_w[n] = t[n][6] # t[n]의 9시방향의 값
    spin(n, d)
    '''n의 왼쪽 톱니바퀴 회전'''
    left = n-1 # 왼쪽에 있는 톱니바퀴
    d_left = d
    while(1<=left and left<=4):
        if t_e[left+1] != -1 and t_w[left+1] != -1: # 이전 톱니바퀴가 회전한 경우
            if t[left][2] != t_w[left+1]: # 맞닿는 부분이 서로 다른경우
                t_e[left] = t[left][2]
                t_w[left] = t[left][6]
                d_left = -d_left # 다음번에 돌땐 반대방향으로 돌아야하므로
                spin(left, d_left)
        left -= 1
    '''n의 오른쪽 톱니바퀴 회전'''
    right = n+1 # 오른쪽에 있는 톱니바퀴
    d_right = d
    while(1<=right and right<=4):
        if t_e[right-1] != -1 and t_w[right-1] != -1: # 이전 톱니바퀴가 회전한 경우
            if t[right][6] != t_e[right-1]: # 맞닿는 부분이 서로 다른경우
                t_e[right] = t[right][2]
                t_w[right] = t[right][6]
                d_right = -d_right # 다음번에 돌땐 반대방향으로 돌아야하므로
                spin(right, d_right)
        right += 1
ans = 0 # 정답 저장
for i in range(1, 5):
    if t[i][0] == '1':
        ans += 1<<(i-1) # 2**(i-1) 과 동일
print(ans)
'''end of main'''