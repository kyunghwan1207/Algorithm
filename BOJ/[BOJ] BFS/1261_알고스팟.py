from collections import deque
import sys, math
input = sys.stdin.readline

def bfs(x, y):
    global n
    global m
    Q = deque()
    Q.append((x, y))
    dist[x][y] = 0
    while len(Q) > 0:
        x, y = Q.popleft()
        # 현재 방향에서 4가지 방향으로 탐색해보기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # M의 인덱스를 벗어날 경우 무시
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if M[nx][ny] == 1 and dist[nx][ny] > dist[x][y] + 1: # 벽을 만났을 때
                Q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1 # 벽을 하나씩 부실 것이므로
            if M[nx][ny] == 0 and dist[nx][ny] > dist[x][y]: # 빈 방일 경우
                Q.append((nx, ny))
                dist[nx][ny] = dist[x][y] # 벽을 안 부실 것이므로
    return dist[n-1][m-1]

'''star of main'''
m, n = map(int, input().split())
dist = [[math.inf]*m for _ in range(n)]
M = []
#     상 하  좌 우
dx = [-1, 1,  0, 0]
dy = [ 0, 0, -1, 1]
for _ in range(n):
    M_temp = []
    s = input().split('\n')[0]
    for i in range(m):
        M_temp.append(int(s[i]))
    M.append(M_temp)
print(bfs(0, 0))
'''end of main'''