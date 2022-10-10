# 1620 ~ 1720
# 주사위 모습 출력
def show():
    for i in range(4):
        if i != 1:
            print(" ", dice_col[i])
        else:
            for j in range(3):
                print(dice_row[j], end = ' ')
            print()
def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= m

# 점수 계산
def bfs(sx, sy):
    q = [[sx, sy]]
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[sx][sy] = True
    res = 1
    val = board[sx][sy]
    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if OOB(nx, ny): continue
            if visited[nx][ny]: continue
            if val != board[nx][ny]: continue
            res += 1
            q.append([nx, ny])
            visited[nx][ny] = True
    return res

# 굴리기
def roll(dd):
    global dice_row, dice_col
    # east
    if dd == 0:
        dr_temp = dice_row[2]
        dc_temp = dice_col[3]
        for i in range(1, -1, -1):
            dice_row[i+1] = dice_row[i]
        dice_row[0] = dc_temp
        dice_col[1] = dice_row[1]
        dice_col[3] = dr_temp
    # south
    elif dd == 1:
        dc_temp = dice_col[3]
        for i in range(2, -1, -1):
            dice_col[i+1] = dice_col[i]
        dice_col[0] = dc_temp
        dice_row[1] = dice_col[1]
    # west
    elif dd == 2:
        dr_temp = dice_row[0]
        dc_temp = dice_col[3]
        for i in range(2):
            dice_row[i] = dice_row[i+1]
        dice_row[2] = dc_temp
        dice_col[3] = dr_temp
        dice_col[1] = dice_row[1]
    # north
    elif dd == 3:
        dc_temp = dice_col[0]
        for i in range(3):
            dice_col[i] = dice_col[i+1]
        dice_col[3] = dc_temp
        dice_row[1] = dice_col[1]


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dice_row = [4, 1, 3] # dice_row[1] == dice_col[1]
    dice_col = [2, 1, 5, 6] # dice_col[3] 이 주사위 아랫면의 정수
    #     e   s   w   n
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    ans = 0
    dir = 0
    nx, ny = 0, 0
    for p in range(k):
        nx, ny = nx + dx[dir], ny + dy[dir]
        if OOB(nx, ny):
            nx, ny = nx - dx[dir], ny - dy[dir]
            dir = (dir+2) % 4 # 반대방향으로 방향전환
            nx, ny = nx + dx[dir], ny + dy[dir]
        roll(dir)
        # print(f"{p}. after roll / dir: {dir} / (nx, ny): ({nx}, {ny})")
        # show()
        cnt = bfs(nx, ny)
        ans += board[nx][ny] * cnt
        if dice_col[3] > board[nx][ny]:
            dir = (dir+1) % 4
        elif dice_col[3] < board[nx][ny]:
            dir = (dir - 1 + 4) % 4
        
    print(ans)
