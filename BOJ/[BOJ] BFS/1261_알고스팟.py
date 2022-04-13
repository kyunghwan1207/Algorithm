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

'''
<알고리즘 설명>
(1,1) 부터 (N, M)대신에 편의상 (0, 0)부터 (N-1, M-1)로 접근.
dx, dy를 통해서 상하좌우 모든 방향으로 이동하면서 벽이거나 빈 방인 경우에 따라서 적절한 로직 수행
최솟값을 유지해야 하기 때문에 
조건문에서 bfs에서 전형적으로 사용하는 방문여부 대신 최솟값으로 업데이트 할 수 있는지 여부를 체크하는 조건으로 대체
Step1. 사용할 변수 초기화 및 할당
Step2. bfs함수 호출후 Queue에 원소가 있는 동안 앞서 설명한 로직 수행

<수행시간 분석>
미로의 크기를 n x m(가로 x 세로), 상수를 c라고 하면
Step1. O(n)
Step2. O(n*m)
=> 총 수행시간: O(n*m)
'''
