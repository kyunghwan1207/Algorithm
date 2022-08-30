import heapq

def dijkstra(start):
    q = heapq()
    distance = [MAX for _ in range(n+1)]
    q.append((0, start))
    distance[start] = 0
    
    while q:
        dist, now = q.popleft()
        if distance[now] < dist: continue
        for node_idx, node_time in graph[now]:
            time = dist + node_time
            if distance[node_idx] > time:
                distance[node_idx] = time
                q.append((time, node_idx))
    return distance
        
if __name__ == "__main__":
    MAX = 2147000000
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t)) # 시작점idx - (끝점, 시간)
        
        
    answer = 0
    for i in range(1, n+1):
        forward = dijkstra(i) # 각 시작점에서 x로 가는 최단 거리
        backward = dijkstra(x) # x에서 각 지점으로 가는 최단거리
        answer = max(answer, forward[x] + backward[i])
    print(answer)
