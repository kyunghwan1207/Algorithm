# 20:30시작 21:00해결 -> 정답
import sys
from collections import deque

def BFS(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, v = map(int, input().rsplit())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        lis = list(map(int, input().split()))
        graph[lis[0]].append(lis[1])
        graph[lis[1]].append(lis[0])
    for i in graph:
        i.sort()
    visited = [False]*(n+1) # 1부터 시작이니까 index맞추기 위함
    DFS(graph, v, visited)
    print() # 줄바꿈용도
    visited = [False]*(n+1)
    BFS(graph, v, visited)
'''
느낀점
1. 양방향이기 때문에 노드표시를 입력받은 값 둘다 시작점으로써 체크해줘야함.
2. 방문순서가 ASC이기 때문에 sort함수를 통해 각 노드의 방문 순서를 고정해줌 
'''