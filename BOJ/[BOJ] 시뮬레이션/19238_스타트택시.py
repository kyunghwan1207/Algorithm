def OOB(x, y):
    return x < 0 or x >=n or y < 0 or y >= n

# 택시가 다음에 태울 손님의 정보 return
def getNextLoc(people_board, x, y):
    q = []
    visited = [[False]*n for _ in range(n)]
    q.append([x, y, 0])
    visited[x][y] = True
    idx = 0
    res = []
    # taxi_x, taxi_y위치에 승객이 존재하는 경우
    if people_board[x][y] != 0:
        res.append([0, x, y, people_board[x][y][0], people_board[x][y][1]])
    while len(q) > idx:
        x, y, cnt = q[idx]
        idx += 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if OOB(nx, ny): continue
            if not visited[nx][ny] and board[nx][ny] != 1:
                if people_board[nx][ny] != 0: res.append([cnt+1, nx, ny, people_board[nx][ny][0], people_board[nx][ny][1]])
                q.append([nx, ny, cnt+1])
                visited[nx][ny] = True
    return res

# (sx, sy)에서 (fx, fy)까지 거리 return
def getDistance(sx, sy, fx, fy):
    q = []
    # 출발지와 목적지가 동일할 경우
    if sx == fx and sy == fy: return 0
    visited = [[False]*n for _ in range(n)]
    q.append([sx, sy, 0])
    visited[sx][sy] = True
    idx = 0
    while len(q) > idx:
        x, y, cnt = q[idx]
        idx += 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if OOB(nx, ny): continue
            if nx == fx and ny == fy: return cnt+1
            if not visited[nx][ny] and board[nx][ny] == 0:
                q.append([nx, ny, cnt+1])
                visited[nx][ny] = True
    # 목적지까지 갈 수 없는 경우
    return -1

if __name__ == "__main__":
    n, m, fuel = map(int, input().split())
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    people_board = [[0] * n for _ in range(n)]
    taxi_x, taxi_y = list(map(int, input().split()))
    taxi_loc = [taxi_x-1, taxi_y-1]
    for _ in range(m):
        start_x, start_y, dest_x, dest_y = map(int, input().split())
        # 승객 있는 곳에 목적지 주소 저장
        people_board[start_x-1][start_y-1] = [dest_x-1, dest_y-1]

    for _ in range(m):
        next_loc = getNextLoc(people_board, taxi_loc[0], taxi_loc[1])
        # 모든 손님을 다 태워 목적지로 안내해서 더이상 태울 손님이 없는 경우
        if len(next_loc) == 0:
            fuel = -1; break
        # 택시가 태울 승객 조건에 맞게 정렬
        next_loc.sort(key = lambda x : [x[0], x[1], x[2]]) # [거리, 행, 열] # default ASC

        dist_toStart, start_x, start_y, dest_x, dest_y = next_loc[0] # 0번째 index가 다음에 태울 손님
        # 손님을 태우러 갈 수 있는 경우
        if fuel > dist_toStart:
            fuel -= dist_toStart
            dist_toDest = getDistance(start_x, start_y, dest_x, dest_y)
            # (start_x, start_y)에서 (dest_x, dest_y)까지 길이 없는 경우
            if dist_toDest == -1:
                fuel = -1; break
            # (start_x, start_y)에서 (dest_x, dest_y)까지 갈 수 있고 연료도 가능한 경우 경우
            if fuel >= dist_toDest:
                people_board[start_x][start_y] = 0 # 승객 삭제
                # fuel -= dist_toDest
                # fuel += 2*dist_toDest
                fuel += dist_toDest # 2*dist_toDest - dist_toDest = dist_toDest
                taxi_loc = [dest_x, dest_y] # 택시 위치 업데이트
            # (start_x, start_y)에서 (dest_x, dest_y)까지 갈 순 있지만 연료가 없는 경우
            else:
                fuel = -1; break
        # 손님을 태우러 갈 수 없는 경우
        else:
            fuel = -1; break
    print(fuel)

'''
느낀점
1. 문제의 흐름에 맞게 매번 택시가 승객 태울때 마다 각 승객의 위치정보를 한번에 구한다음에
그 next_loc[][] 에서 태우러 갈 조건에 맞게 정렬 후 해당 승객을 태움처리
2. next_loc[][]가 [] 일 때 즉, 택시가 다음에 태울 승객이 존재하지 않을 가능성도 고려하자
3. getDistance(sx, sy, fx, fy)에서 return 값이 -1일 때 즉, 출발지-도착지가 막혀있을 때도 고려하자
'''
