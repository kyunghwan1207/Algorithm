# 1420 ~
def show_board(board):
    for i in range(n):
        print()
        for j in range(n):
            print(board[i][j], end = ' ')
    print()

def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= n


def move_biz():
    global s, board
    sstep, bstep = 1, 1 # 채워질 곳, 채울 구슬
    sflag, bflag = 0, 0
    sd, bd = 0, 0
    snx, sny = s, s
    bnx, bny = s, s
    while True:
        slist = get_pos(snx, sny, sd, sstep)
        blist = get_pos(bnx, bny, bd, bstep)
        if len(blist) == 0: return
        snx, sny, sd, sstep = slist[0], slist[1], slist[2], slist[3]
        bnx, bny, bd, bstep = blist[0], blist[1], blist[2], blist[3]


def get_pos(x, y, d, flag, step):
    # step = 1
    # d, flag = 0, 0
    # nx, ny = s, s
    global dx, dy
    nx, ny = x + dx[d], y + dy[d]
    if OOB(nx, ny): return []

    if step-1 == 0:
        print('enter 1-if')
        d = (d + 1) % 4
        flag += 1
        if flag != 0 and flag % 2 == 0:
            step += 1
    return [nx, ny, d, flag, step]


def break_biz(d, z):
    global s, cnt_list, board
    #     0, n   s    w    e
    bx = [0, -1, 1, 0,  0]
    by = [0, 0, 0, -1, 1]
    nx, ny = s, s
    while z:
        nx, ny = nx + bx[d], ny + by[d]
        if OOB(nx, ny): break
        cnt_list[board[nx][ny]] += 1
        board[nx][ny] = 0
        z -= 1


if __name__ == "__main__":
    n,m = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    command = [list(map(int, input().split())) for _ in range(m)]
    cnt_list = [0] * 4 # [0, {폭발한 1번 구슬의 개수}, {폭발한 2번 구슬의 개수}, {폭발한 3번 구슬의 개수}]
    # 1, 2, 3, 4 : 'u(n) 3' 'd(s) 1' 'l(w) 0' 'r(e) 2'
    #    w   s   e   n
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    s = int((n+1)/2 - 1)
    # for i in range(m):
    #     # 블리자드 마법 시전
    #     break_biz(command[i][0], command[i][1])
    #     # 구슬 빈칸 채우기 이동
    #     move_biz()
    #     # 구슬 폭발 (동시에 폭발)
    #
    #     # 이동 후 폭발가능하면 폭발하기 반복
    #     # 구슬 변화하기
    check_board = [[0 for _ in range(n)] for _ in range(n)]
    step = 1
    d, flag = 0, 0
    nx, ny = s, s
    val = 1
    while True:
        clist = get_pos(nx, ny, d, flag, step)
        if len(clist) == 0: show_board(check_board); exit(0)
        nx, ny, d, flag, temp_step = clist[0], clist[1], clist[2], clist[3], clist[4]
        print('return: ', nx, ny, d, flag, temp_step)
        step = max(step, temp_step)
        print('after: ', nx, ny, d, flag, step)
        check_board[nx][ny] = val
        val += 1
    # 뱅글뱅글 돌면서 문제의 예시 그림처럼 값 저장 가능
    # while True:
    #     for st in range(step):
    #         nx, ny = nx + dx[d], ny + dy[d]
    #         if OOB(nx, ny): show_board(check_board); exit(0)
    #         check_board[nx][ny] = val
    #         val += 1
    #     d = (d+1) % 4
    #     flag += 1
    #     if flag != 0 and flag % 2 == 0:
    #         step += 1
