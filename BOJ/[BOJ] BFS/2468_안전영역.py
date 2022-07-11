# 1030 start -> 1130 solve -> 76% success -> 100% success(range(100)으로 수정)
import sys
from collections import deque

def BFS(loc, h):
    global visited, board, dx, dy, n
    # q가 비워지는 횟수를 카운트
    x, y = loc
    q = deque()
    visited[x][y] = True
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if not visited[nx][ny] and board[nx][ny] > h:
                visited[nx][ny] = True
                q.append((nx, ny))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    visited = [[False for _ in range(n)] for _ in range(n)]
    #     e    n   w    s
    dx = [0,   1,  0,   -1]
    dy = [1,   0,  -1,   0]
    ans = 0
    cnt = 0
    for h in range(100):
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and board[i][j] > h:
                    BFS((i, j), h)
                    cnt += 1
        if cnt == 0: print(ans); exit(0)
        ans = max(ans, cnt)
        visited = [[False for _ in range(n)] for _ in range(n)]
        cnt = 0
    print(ans)

'''
느낀점
1. "아무곳도 안잠길 수도 있다" 즉, 비가 내리지 않는 경우를 고려해야함.
'''
