def OOB(x, y):
    global N
    return x < 0 or x >= N or y < 0 or y >= N


# 각 지역에 국가idx를 표시함
def bfs(sx, sy, idx):
    global A, N, L, R, visited, sum_list, cnt_list
    q = []
    q.append([sx, sy])
    visited[sx][sy] = idx
    sum_list[idx] = A[sx][sy]
    cnt_list[idx] = 1
    # q_idx = 0
    while q: # while q == while len(q) == while len(q) != 0
        x, y = q.pop(0) # q.pop(0) == q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if OOB(nx, ny): continue
            val = abs(A[nx][ny] - A[x][y])
            if visited[nx][ny] == -1 and L <= val <= R:
                q.append([nx, ny])
                visited[nx][ny] = idx
                cnt_list[idx] += 1
                sum_list[idx] += A[nx][ny]


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    A = []
    #   e   n  w  s
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    day = 0
    is_update = True
    for _ in range(N):
        A.append(list(map(int, input().split())))
    while is_update:
        is_update = False
        u_idx = -1
        sum_list = [0 for _ in range(2500)]
        cnt_list = [0 for _ in range(2500)]
        visited = [[-1 for _ in range(N)] for _ in range(N)] # 연합idx 표시
        for i in range(N):
            for j in range(N):
                if visited[i][j] == -1:
                    u_idx += 1
                    bfs(i, j, u_idx)
        # // visited[][]에 국가 및 연합표시 완료
        # avg 값으로 업데이트 하자
        for i in range(N):
            for j in range(N):
                if visited[i][j] != -1:
                    idx = visited[i][j]
                    avg = sum_list[idx]//cnt_list[idx]
                    if A[i][j] != avg:
                        is_update = True
                        A[i][j] = avg
        if is_update:
            day += 1

    print(day)

'''
<느낀점>
1. 연합을 표시한다는 느낌보단 나라나라를 표시해준다고 생각하자
2. bfs쓸때는 if OOB: continue 쓰고
3. 변수 컨트롤 어려워보이면 나라의 최대 수만큼 배열 만들어놓고 기록하자
4. 시작점을 찾으려고 하지말고 모두다 시작점으로 넣어보면서 기록하자 (u_idx++시키면서)
'''