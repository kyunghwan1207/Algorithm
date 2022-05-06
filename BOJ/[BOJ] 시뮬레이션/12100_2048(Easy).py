# 90도 회전시키는 함수
def rotate():
    global board2, N
    temp_board2 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp_board2[i][j] = board2[i][j]
    for i in range(N):
        for j in range(N):
            board2[i][j] = temp_board2[N-1-j][i]
    return

# 왼쪽으로 밀어서 board2-update하기
def push_to_left(dir):
    global board2, N
    while dir > 0: # 90도만큼 계획회전
        dir -= 1
        rotate()
    for i in range(N): # 행
        temp_board2 = [0 for _ in range(N)]
        idx = 0  # temp_board2에 삽입할 or 최근에 삽입한 원소의 위치 가르킴
        for j in range(N): # 열
            if board2[i][j] == 0: continue # 0일땐 무시
            # 0이 아닐때 아래 경우 수행
            if temp_board2[idx] == 0:
                temp_board2[idx] = board2[i][j]
            elif temp_board2[idx] == board2[i][j]:
                temp_board2[idx] *= 2
                idx += 1
            else:
                idx += 1
                temp_board2[idx] = board2[i][j]

        for j in range(N):
            board2[i][j] = temp_board2[j]
    return


if __name__ == '__main__':
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    board2 = [[0 for _ in range(N)] for _ in range(N)]
    # board = [0, 2, 0, 2, 8, 8, 0, 16]
    # 4^5 의 경우가 있다 = 2^10 = 1024
    max_val = -2147000000
    for tmp in range(1<<10):
        for i in range(N):
            for j in range(N):
                board2[i][j] = board[i][j]
        brute = tmp
        # 동, 서, 남, 북 모든 경우의 수 해보기
        for i in range(5):
            dir = brute % 4
            brute /= 4
            push_to_left(dir) 
        for i in range(N):
            for j in range(N):
                max_val = max(max_val, board2[i][j])
    print(max_val)

'''
느낀점
1. 반복적인 코드 대신에 코드의 함수를 통한 재활용성을 높이자
ex. 위,아래,왼쪽,오른쪽을 별도로 짜지 않고 왼쪽으로 밀기(push_to_left)하나만 짜고 
나머지의 경우에는 90도 회전시키는 함수의 호출횟수로 조정해서 push_to_left함수를 적용

2. 기존 배열에서 다른 모습을 취할때 무조건 새로운 배열을 하나 두고 풀자
그러고 나서 다시 copy 함으로써 원래 배열로 복구하자 
'''