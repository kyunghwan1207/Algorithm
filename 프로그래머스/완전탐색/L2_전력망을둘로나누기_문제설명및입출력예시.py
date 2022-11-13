# 노드 방문 처리(visited[] 업데이트)
def dfs(visited, v, ex_edge, graph):
    for node in graph[v]:
        if v in ex_edge and node in ex_edge: continue
        if not visited[node]:
            visited[node] = True
            dfs(visited, node, ex_edge, graph)    
            
    return visited

# 방문한 노드의 개수 구하기(visited[]배열의 true 처리로 인해 방문노드 개수 구하기 어려움)
def getCount(visited):
    res = 0
    for v in visited:
        if v: 
            res += 1
    if res == 0: 
        res = 1
        
    return res
    
def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for s, e in wires:
        graph[s].append(e) 
        graph[e].append(s)
    cnt = 2147000000
    
    for i in range(len(wires)):
        # 연결을 끊어볼 간선
        ex_s, ex_e = wires[i]
        
        visited = [False] * (n+1)
        visited = dfs(visited, ex_s, wires[i], graph)
        first_cnt = getCount(visited)
        
        visited = [False] * (n+1)
        visited = dfs(visited, ex_e, wires[i], graph)
        second_cnt = getCount(visited)
        
        cnt = min(cnt, abs(first_cnt-second_cnt))
        
    return cnt
