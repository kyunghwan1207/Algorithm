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

'''
<알고리즘 설명>
방문여부를 체크하는 리스트(visited), 해당지점까지 가는데 걸리는 시간을 저장하는 리스트(dist)로 놓고 진행
Step1. 최대값이 100000이기 때문에 인덱스로 접근을 쉽게하기 위해 visited, dist를 100001크기로 리스트 정의
Step2. bfs함수를 통해 현재 방문한 점에 방문처리하고 인접한 점에 대해 방문처리와 dist값을 업데이트 실행(모든 경우를 다 해봐야하므로 if로만 로직구현)

<수행시간 분석>
수빈이의 현재 점을 n, 동생의 점을 k, 상수를 c라고 하면
Step1. O(c)
Step2. O(abs(k-n)) (이유: -1씩 가까워지는 것이 최악의 경우이기 때문)
=> 총 수행시간: O(abs(k-n))
'''
