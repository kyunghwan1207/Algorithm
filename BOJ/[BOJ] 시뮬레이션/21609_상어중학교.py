# 2100 ~ 2330
from collections import deque

def show_board(arr):
    for i in range(n):
        print()
        for j in range(n):
            print(arr[i][j], end=' ')
    print()
    
def gravity():
    for j in range(n):
        temp_board = [-2 for _ in range(n)]
        ptr = n-1
        for i in range(n-1, -1, -1):
            if board[i][j] == -2: continue
            if board[i][j] == -1:
                temp_board[i] = -1
                ptr = i-1
            else:
                temp_board[ptr] = board[i][j]
                ptr -= 1
        for k in range(n):
            board[k][j] = temp_board[k]

def rotate_90():
    global board
    temp_board = [[-2 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp_board[n-1-i][j] = board[j][i]
    for i in range(n):
        for j in range(n):
            board[i][j] = temp_board[i][j]

def OOB(x, y):
    return x < 0 or x>=n or y < 0 or y >= n

def bfs(x, y, val):
    global pos, visited
    q = deque()
    q.append((x, y))
    pos.append([x, y])
    cnt = 1
    rainbow_cnt = 0
    while q:
        # print('q: ', q)
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if OOB(nx, ny): continue
            if visited[nx][ny]: continue
            if board[nx][ny] == val or board[nx][ny] == 0:
                if board[nx][ny] != 0:
                    visited[nx][ny] = True
                elif board[nx][ny] == 0:
                    visited[nx][ny] = True
                    rainbow_cnt += 1
                q.append((nx, ny))
                pos.append([nx, ny])
                cnt += 1
    return cnt, rainbow_cnt

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    #    e  n   w   s
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    answer = 0

    while True:
        pos = []
        max_pos = []
        max_rainbow_cnt = 0
        max_cnt = 0
        visited = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] > 0 and not visited[i][j]:
                    visited[i][j] = True
                    pos = []
                    temp_cnt, temp_rainbow_cnt = bfs(i, j, board[i][j])
                    # 0 이었던 부분은 다시 방문할 수 있게 만듦
                    for lis in pos:
                        if board[lis[0]][lis[1]] == 0:
                            visited[lis[0]][lis[1]] = False
                    if temp_cnt < 2: continue
                    if max_cnt < temp_cnt:
                        max_cnt = temp_cnt
                        max_rainbow_cnt = temp_rainbow_cnt
                        max_pos = pos
                    elif max_cnt == temp_cnt and max_rainbow_cnt <= temp_rainbow_cnt:
                        max_rainbow_cnt = temp_rainbow_cnt
                        max_pos = pos
                    elif max_cnt == temp_cnt and max_rainbow_cnt > temp_rainbow_cnt: continue

        answer += max_cnt**2
        if len(max_pos) == 0: print(answer); break
        for lis in max_pos: # 삭제
            board[lis[0]][lis[1]] = -2
            
        gravity()
        rotate_90()
        gravity()
