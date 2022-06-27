import sys

def OOB(x, y):
    global n
    return x < 0 or x >= n or y < 0 or y >= n

def spread(r, c, d):
    global board, n, dr, dc, spread_direction_list, ans
    dirs = spread_direction_list[d]
    remain_sand = board[r][c] # 일정 p로 분배 후 남은 모래양 기록
    for dir in dirs:
        x, y, p = dir[0], dir[1], dir[2]
        nr, nc = r+x, c+y
        if OOB(nr, nc):
            ans += int(board[r][c]*p)
            remain_sand -= int(board[r][c]*p)
            continue
        board[nr][nc] += int(board[r][c]*p)
        remain_sand -= int(board[r][c]*p)
    nr, nc = r+dr[d], c+dc[d] # 문제상 a표시 좌표로 이동
    if OOB(nr, nc):
        ans += remain_sand
    else:
        board[nr][nc] += remain_sand
    board[r][c] = 0


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    nr, nc = n//2, n//2
    #     w   n   e  s
    dr = [0,  1,  0,  -1]
    dc = [-1,  0,  1,  0]
    # 문제의 y표시 기준으로 좌표이동값 설정
    west = [(-1, 1, 0.01), (1, 1, 0.01), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02),
            (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05)]
    north = [(y*-1, x, p) for x, y, p in west]
    south = [(x*-1, y*-1, p) for x, y, p in north]
    east = [(x*-1, y*-1, p) for x, y, p in west]
    spread_direction_list = [west, north, east, south]
    step, k, d = 0, 0, 0
    ans = 0

    for i in range(2*n-1):
        d = i%4
        if d == 0 or d == 2:
            step += 1
        for _ in range(step):
            temp = board[nr][nc]
            board[nr][nc] = 0
            nr, nc = nr + dr[d], nc + dc[d]
            board[nr][nc] += temp
            spread(nr, nc, d)
    print(ans)
