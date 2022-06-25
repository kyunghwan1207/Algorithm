# 2230시작 2430완료 정답

# 이동하려는 위치 (r,c)가 격자 범위를 벗어나는지/아닌지 -> T/F
def OOB(r, c):
    global n
    return r < 0 or r >= n or c < 0 or c >= n

#입력: 문제에서 x표시의 좌표 r, c와 이동한 방향 d
def spread(r, c, d):
    global board, ans, dr, dc # ans가 최종정답값
    # d-> 0 w, 1 s, 2 e, 3 n
    du = (d+1+4) % 4 # x기준 위방향(n)
    dd = (d-1+4) % 4 # x기준 아래방향(s)
    nr, nc = r + dr[d], c + dc[d] # y좌표
    sand = board[r][c] + board[nr][nc]
    board[r][c] = 0
    # 1% 처리
    nru, ncu = r + dr[du], c + dc[du]
    nrd, ncd = r + dr[dd], c + dc[dd]
    if OOB(nru, ncu): ans += int(sand*0.01)
    else: board[nru][ncu] += int(sand*0.01)
    if OOB(nrd, ncd): ans += int(sand*0.01)
    else: board[nrd][ncd] += int(sand * 0.01)
    # 2%, 7% 처리
    nru, ncu = nru + dr[d], ncu + dc[d]
    nrd, ncd = nrd + dr[d], ncd + dc[d]
    nruu, ncuu = nru+dr[du], ncu+dc[du]
    nrdd, ncdd = nrd+dr[dd], ncd+dc[dd]
    if OOB(nru, ncu): ans += int(sand*0.07)
    else: board[nru][ncu] += int(sand*0.07)
    if OOB(nrd, ncd): ans += int(sand * 0.07)
    else: board[nrd][ncd] += int(sand*0.07)
    if OOB(nruu, ncuu): ans += int(sand*0.02)
    else: board[nruu][ncuu] += int(sand*0.02)
    if OOB(nrdd, ncdd): ans += int(sand * 0.02)
    else: board[nrdd][ncdd] += int(sand*0.02)
    # 10% 처리
    sand_remain = sand - (2 * int(sand * 0.01) + 2 * int(sand * 0.02) + 2 * int(sand * 0.07) + 2 * int(sand * 0.10) + int(sand * 0.05))  # y에 있는 모래의 양
    nnr, nnc = nr+dr[d], nc+dc[d] # a위치
    board[nr][nc] = 0 # y의 모래 이동을 위해 기존의 모래없애기
    if OOB(nnr, nnc): ans += int(sand_remain) # a가 격자를 벗어날 경우
    else: board[nnr][nnc] += int(sand_remain)
    nru, ncu = nru + dr[d], ncu + dc[d]
    nrd, ncd = nrd + dr[d], ncd + dc[d]
    if OOB(nru, ncu): ans += int(sand*0.10)
    else: board[nru][ncu] += int(sand*0.10)
    if OOB(nrd, ncd): ans += int(sand * 0.10)
    else: board[nrd][ncd] += int(sand*0.10)
    # 5% 처리
    nnnr, nnnc = nnr + dr[d], nnc + dc[d]
    if OOB(nnnr, nnnc): ans += int(sand*0.05)
    else: board[nnnr][nnnc] += int(sand*0.05)

if __name__ == "__main__":
    n = int(input())
    board = []
    ans = 0 # 격자를 벗어난 모래의 양
    for _ in range(n):
        board.append(list(map(int, input().split())))
    sr, sc = n//2, n//2 # 시작점
    #     w     s     e    n
    dr = [0,    1,    0,    -1]
    dc = [-1,   0,    1,    0]
    # n=7, 1 1 2 2 3 3 4 4 5 5 6 6
    step, t, d = 1, 0, 0
    while True:
        for _ in range(step):
            spread(sr, sc, d % 4)
            sr, sc = sr + dr[d%4], sc + dc[d%4]
            if sr == 0 and sc == 0: print(ans); exit(0)
        d += 1
        t += 1
        if t % 2 == 0:
            step += 1
'''
느낀점
1. step은 방향d로 나아갈 횟수를 의미함
하지만 step이 1, 1, 2, 2, 3, 3 ... 와 같이 임의의 패턴을 가지고 있어서
t라는 변수를 별도로 두어서 방향d로의 이동이 완료될때 마다 t++시켜서 
t가 짝수일 경우에 step ++시키는 방법으로 구현
'''

