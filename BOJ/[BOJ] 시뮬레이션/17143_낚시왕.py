import sys
input = sys.stdin.readline

def show_board(arr, R, C):
    for i in range(R):
        print()
        for j in range(C):
            if arr[i][j] != 0:
                print(arr[i][j][2], end = ' ')
            else:
                print(0, end = ' ')
    print()
    return

# 범위 벗어나는지/아닌지 -> T/F
def OOB(r, c):
    global R, C
    return r < 0 or r >= R or c < 0 or c >= C

# 상어 이동한 것을 temp에 기록 후 기록완료된 temp를 return
def move():
    global board, R, C, M, dr, dc
    temp = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0: # 움직이기 시작!
                # d: 0-north, 1-south, 2-east, 3-west
                board_val = board[i][j] # [s, d, z]
                board[i][j] = 0
                r, c = i, j
                s = board_val[0]
                d = board_val[1]
                while s > 0:
                    r += dr[d]
                    c += dc[d] 
                    if not OOB(r, c): # 방향유지
                        s -= 1
                    else: # 방향 전환
                        # 0 or 맨마지막 칸에서 다시 s 만큼 바뀐 d방향으로 전진 진행하기 위한 설정
                        r -= dr[d]
                        c -= dc[d]
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                # 한마리의 상어 이동이 완료된 경우 (r, c) -> s 모두 소진
                board_val[1] = d # 바뀐방향 할당 # [s, d, z]
                if temp[r][c] != 0: # 이미 그 칸에 다른 상어가 존재할 경우 먹히는 과정진행
                    if temp[r][c][2] < board_val[2]:
                        temp[r][c] = board_val
                    # else: temp 그대로 유지 -> board가 잡아먹힘
                else: # 해당 칸에 상어가 없는 경우
                    temp[r][c] = board_val
    return temp


if __name__ == "__main__":
    R, C, M = map(int, input().split())
    board = [[0 for _ in range(C)] for _ in range(R)]
    if M == 0: print(0); exit(0)
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        board[r-1][c-1] = [s, d-1, z] # 상어정보 입력
    # d: 0-north, 1-south, 2-east, 3-west
    size = 0
    # 0-north, 1-south, 2-east, 3-west
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    for j in range(C): # 1. 한칸 이동
        for i in range(R):
            # j는 사람의 위치
            # i는 땅에서 부터 점차 멀어짐
            if board[i][j] != 0:
                size += board[i][j][2] # 2. 상어잡기
                board[i][j] = 0 # 3. 상어 사라짐
                break
        board = move() # 4. 상어이동
    print(size)

'''
<느낀점>
1. for문에서 인자는 무조건 건드리지 말자 -> i, j는 조작x
2. 문제에서 제시한 조건 순서대로 진행할 수 있도록 노력하자
'''