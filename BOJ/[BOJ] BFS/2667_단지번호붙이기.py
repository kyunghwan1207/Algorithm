# 1513 -> 1535 성공
import sys
from collections import deque

def OOB(x, y):
    global n
    return x < 0 or x >= n or y< 0 or y >= n

def BFS(i, j):
    global board, dx, dy, n, visited, ans, cnt
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    ans += 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if OOB(nx, ny): continue
            if not visited[nx][ny] and board[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    board = []
    for _ in range(n):
        input_ = input()
        input_ = input_.split('\n')[0]
        board.append([])
        for i in input_:
            board[-1].append(int(i))
    #     e  s   w   n
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False for _ in range(n)] for _ in range(n)]
    ans = 0 # 총 단지 수
    ans_list = [] # 각 단지의 집 수 저장 리스트
    cnt = 1 # 각 단지의 집 수
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == 1:
                BFS(i, j) # update cnt
                ans_list.append(cnt)
                cnt = 1
    print(ans)
    ans_list.sort()
    for i in range(len(ans_list)):
        print(ans_list[i])

