from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, k):
    global visited
    global dist
    Q = deque()
    Q.append(n)
    visited[n] = True
    dist[n] = 0
    #  팝 <- [a, b, c] <- 삽입 # append
    #  삽입-> # appendleft() -> 팝 # popright
    while len(Q) > 0:
        x = Q.popleft()
        if x == k: break
        if 2*x < MAX and visited[2*x] == False: # 2*x 방문
            Q.append(2*x)
            visited[2*x] = True
            dist[2*x] = dist[x] # 0초 소요되므로
        if x-1 >= 0 and visited[x-1] == False: # x-1 방문
            Q.append(x-1)
            visited[x-1] = True
            dist[x-1] = dist[x] + 1
        if x+1 < MAX and visited[x+1] == False: # x+1 방문
            Q.append(x+1)
            visited[x+1] = True
            dist[x+1] = dist[x] + 1
    return dist[k]

'''start of main'''
MAX = 100001 # final value
n, k = map(int, input().split())
visited = [False]*MAX # False은 방문x, True은 방문o
dist = [0]*MAX # i번째 인덱스에는 dist[i]까지 가는데 걸리는 시간저장
print(bfs(n, k))
'''end of main'''