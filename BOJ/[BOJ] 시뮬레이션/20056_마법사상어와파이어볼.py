# [1430 시작] 1630제출-> 시간초과
# [1700 수정] 파이어볼이 소멸될때, r, c = -1, -1로 바꾸는 것 대신 pop을 통해 리스트에서 제거시킴 -> 정답!
def split_fire_ball(r, c):
    global fire_ball, board, n
    sum_m, sum_s = 0, 0
    odd_cnt, even_cnt = 0, 0
    idx_list = []
    for i in range(len(fire_ball)):
        if fire_ball[i][0] == r and fire_ball[i][1] == c:
            # fire_ball[i][0], fire_ball[i][1] = -1, -1
            board[r][c] -= 1
            idx_list.append(i)
            sum_m += fire_ball[i][2]
            sum_s += fire_ball[i][3]
            if fire_ball[i][4] % 2 == 1:
                odd_cnt += 1
            else:
                even_cnt += 1
    t = 0
    for idx in idx_list:
        idx -= t
        fire_ball.pop(idx)
        t += 1
    if sum_m // 5 == 0:
        # 파이어볼 소멸
        return
    else:
        start_d = 0
        if odd_cnt != 0 and even_cnt != 0:
            start_d = 1
        for _ in range(4):
            temp_ball = [0, 0, 0, 0, 0]
            board[r][c] += 1
            temp_ball[0], temp_ball[1], temp_ball[2], temp_ball[3], temp_ball[4] = \
            r, c,  sum_m // 5, sum_s//(odd_cnt+even_cnt), start_d
            fire_ball.append(temp_ball)
            start_d += 2

# board벗어났을 때 앞으로 가야할 좌표를 알려줌
def OOB(r, c):
    global board, n
    nr, nc = 0, 0
    # north-n
    if r < 0 and c >= 0 and c <= n-1:
        nr, nc = n-1, c
    # north-e
    elif r < 0 and c > n-1:
        nr, nc = n-1, 0
    # north-w
    elif r < 0 and c < 0:
        nr, nc = n-1, n-1
    # east
    elif r >= 0 and r <= n-1 and c > n-1:
        nr, nc = r, 0
    # south
    elif r > n-1 and c <= n-1 and c >= 0:
        nr, nc = 0, c
    # south-e
    elif r > n-1 and c > n-1:
        nr, nc = 0, 0
    # south-w
    elif r > n-1 and c < 0:
        nr, nc = 0, n-1
    # west
    elif r >= 0 and r <= n-1 and c < 0:
        nr, nc = r, n-1
    # not OOB
    else:
        nr, nc = r, c
    return nr, nc


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(n)]
    #     0   1  2   3  4   5   6   7
    dr = [-1, -1, 0, 1, 1,  1,  0,  -1]
    dc = [0,   1, 1, 1, 0, -1, -1,  -1]
    input_ = []
    fire_ball = [] # [r, c, m, s, d]
    for _ in range(m):
        input_ = list(map(int, input().split()))
        input_[0] -= 1
        input_[1] -= 1
        fire_ball.append(input_)
        board[input_[0]][input_[1]] += 1
    for _ in range(k):
        for idx in range(len(fire_ball)):
            r, c, m, s, d = \
            fire_ball[idx][0], fire_ball[idx][1], fire_ball[idx][2], fire_ball[idx][3], fire_ball[idx][4]
            # if r != -1 and c != -1:
            board[r][c] -= 1
            temp_s = s
            nr, nc = r, c
            while temp_s:
                temp_s -= 1
                nr, nc = OOB(nr+dr[d], nc+dc[d])
            board[nr][nc] += 1
            fire_ball[idx][0], fire_ball[idx][1] = nr, nc
        for i in range(n):
            for j in range(n):
                if board[i][j] > 1:
                    split_fire_ball(i, j)
    res = 0
    for i in range(len(fire_ball)):
        # if fire_ball[i][0] != -1 and fire_ball[i][1] != -1:
        res += fire_ball[i][2]
    print(res)
'''
느낀점
1. n보다는 k가 크니까 fire_ball리스트의 크기가 커진다 
따라서 fire_ball을 소멸시킬때 r, c = -1, -1로 만들지말고 pop을 통해 직접적으로 리스트에서 제거하자
'''


