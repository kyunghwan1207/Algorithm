from collections import deque

# 벽을 한 줄 아래로 이동시키는 함수
def move_wall():
    global M, n
    for i in range(n-1, 0, -1):
        for j in range(n):
            M[i][j] = M[i-1][j]
    # 한줄 아래로 이동 후 맨 위 빈방으로 초기화
    for j in range(n):
        M[0][j] = '.'

def bfs(r, c):
    global M, dx, dy, n, visited
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while len(q) > 0:
        visited = [[False for _ in range(n)] for _ in range(n)] # 벽이 움직일때 마다 초기화 필요
        for _ in range(len(q)):
            x, y = q.popleft()
            if x == 0: return True # x가 0이라면 더이상 벽의 영향을 받지 않음
            if M[x][y] == '#': continue
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx > 7 or nx < 0 or ny > 7 or ny < 0: continue
                if M[nx][ny] == '#': continue
                if visited[nx][ny]: continue
                q.append((nx, ny))
                visited[nx][ny] = True
        move_wall()
    return False

'''start of main'''
n = 8
M = []
for _ in range(n):
    M.append([c for c in input()])
visited = [[False for _ in range(n)] for _ in range(n)]
#     상, 하, 좌, 우, 우상, 우하, 좌상, 좌하, 제자리
dx = [-1, 1,  0,  0,  -1,    1,   -1,   1,    0]
dy = [ 0, 0, -1,  1,   1,    1,   -1,  -1,    0]
# 탈출할 수 있으면 1, 없으면 0 출력
if bfs(7, 0):
    print(1)
else:
    print(0)
'''end of main'''