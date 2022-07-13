import sys
from collections import deque

def BFS(start):
    global graph, visited, ans
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
                ans += 1

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    visited = [False for _ in range(n+1)]
    ans = 0
    BFS(1)
    print(ans)

