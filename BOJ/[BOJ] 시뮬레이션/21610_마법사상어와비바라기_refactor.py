def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def copyWater(board, new_cloud_loc):
    #     wn  ne  es  sw
    ddx = [-1, -1, 1, 1]
    ddy = [-1, 1, 1, -1]
    temp_board = [[0]*n for _ in range(n)]
    for cloud in new_cloud_loc:
        x, y = cloud
        for d in range(4):
            nx, ny = x + ddx[d], y + ddy[d]
            if OOB(nx, ny): continue
            if board[nx][ny] > 0:
                temp_board[x][y] += 1

    for x in range(n):
        for y in range(n):
            board[x][y] += temp_board[x][y]
    return board

def generateCloud(board, cloud_history, m):
    cloud = []
    for x in range(n):
        for y in range(n):
            if cloud_history[x][y] != m and board[x][y] >= 2:
                cloud.append([x, y])
                board[x][y] -= 2
    return cloud

if __name__ == "__main__":
    n, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    #    w    wn  n  ne  e  se  s  sw
    dx = [0, -1, -1, -1, 0, 1, 1,  1]
    dy = [-1, -1, 0,  1, 1, 1, 0, -1]
    cloud_loc = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
    cloud_history = [[-1] * n for _ in range(n)] # 몇 번째 m에 방문했는지 표시
    for m in range(M):
        d, s = map(int, input().split())
        d -= 1
        new_cloud_loc = []

        for cloud in cloud_loc:
            nx, ny = cloud
            nx = (nx + dx[d]*s)%n
            ny = (ny + dy[d]*s)%n
            new_cloud_loc.append([nx, ny])
            cloud_history[nx][ny] = m
        for cloud in new_cloud_loc:
            x, y = cloud
            board[x][y] += 1

        board = copyWater(board, new_cloud_loc)

        cloud_loc = generateCloud(board, cloud_history, m)

    ans = 0
    for x in range(n):
        for y in range(n):
           ans += board[x][y]
    print(ans)
