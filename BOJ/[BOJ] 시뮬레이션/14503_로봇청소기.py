def clean(r, c, d):
    global board, dr, dc
    board[r][c] = -1 # Step1
    for _ in range(4):
        nd = (d+3)%4
        nr = r + dr[nd] # 왼쪽으로 회전 Step2
        nc = c + dc[nd]
        if board[nr][nc] == 0:
            clean(nr, nc, nd)
            return
        d = nd
    nd = (d+2)%4
    nr = r + dr[nd]
    nc = c + dc[nd]
    if board[nr][nc] == 1: return
    clean(nr, nc, d)


if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    # 빈칸-0, 벽-1
    #     0-n  1-e 2-s  3-w
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    # 왼쪽이니까 -- 으로 움직임
    clean(r, c, d)
    cnt = 0
    clean_cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == -1:
                clean_cnt += 1
    print(clean_cnt)
