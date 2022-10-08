# 1420 ~ 1630
def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def show(b1d):
    global n
    tboard = [[0 for _ in range(n)] for _ in range(n)]
    tlist = list(board_map.keys())

    for i in range(n*n-1):
        r, c = tlist[i][0], tlist[i][1]
        tboard[r][c] = b1d[board_map.get((r, c))]
    for i in range(n):
        print()
        for j in range(n):
            print(tboard[i][j], end=' ')
    print()

def break_biz(d, z):
    global s, cnt_list
    #     0, n   s    w    e
    bx = [0, -1, 1, 0,  0]
    by = [0, 0, 0, -1, 1]
    nx, ny = s, s
    while z:
        nx, ny = nx + bx[d], ny + by[d]
        if OOB(nx, ny): break
        idx = board_map.get((nx,ny))
        # cnt_list[board1d[idx]] += 1 # 파괴된 x 폭발한 o
        board1d[idx] = 0
        z -= 1
    # print('after_break_biz/board1d: ', board1d)
    # show(board1d)


def move_biz():
    global board1d, s
    nx, ny = s, s
    ridx = 0 # board1d룰 가리키는 idx
    # print('before_move_board1d: ', board1d)
    board1d_temp = [0] * (n*n-1)
    tidx = 0 # board1d_temp를 가리키는 idx
    for i in range(len(board1d)):
        if board1d[i] == 0:
            continue
        board1d_temp[tidx] = board1d[i]
        tidx += 1
    board1d = [0] *(n*n - 1)
    for i in range(len(board1d)):
        board1d[i] = board1d_temp[i]
    # print('after_move_board1d: ', board1d)
    # show(board1d)


if __name__ == "__main__":
    n,m = map(int,input().split())
    board2d = [list(map(int, input().split())) for _ in range(n)]
    command = [list(map(int, input().split())) for _ in range(m)]
    cnt_list = [0] * 4 # [0, {폭발한 1번 구슬의 개수}, {폭발한 2번 구슬의 개수}, {폭발한 3번 구슬의 개수}]
    # 1, 2, 3, 4 : 'u(n) 3' 'd(s) 1' 'l(w) 0' 'r(e) 2'
    #    w   s   e   n
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    s = int((n+1)/2 - 1)
    board_map = {} # { (row, col): 일차원 리스트의 index }
    board1d = [0] * (n*n - 1) # 일차원 리스트

    # // board2d 정보를 board1d로 저장하고 board_map으로 2d좌표->1d인덱스로 매핑정보 저장
    pattern = 0
    step = 1
    flag = True
    val, d = 0, 0
    nx, ny = s, s
    while flag:
        for st in range(step):
            nx, ny = nx + dx[d], ny + dy[d]
            if OOB(nx, ny):
                flag = False
                break
            board_map[(nx, ny)] = val
            board1d[val] = board2d[nx][ny]
            val += 1
        d = (d+1) % 4
        pattern += 1
        if pattern != 0 and pattern % 2 == 0:
            step += 1

    for t in range(m):
        # 구슬 파괴
        break_biz(command[t][0], command[t][1])
        # 구슬 빈칸 채우기 이동
        move_biz()
        # 구슬 폭발 (동시에 폭발)
        fflag = True
        c = 0
        while fflag:
            c += 1
            sidx, cnt = 0, 1
            num = board1d[sidx]
            fflag = False
            '''이미 num을 board1d[0]으로 잡았으니까 [1 ~ len(board1d)-1] 범위만 탐색하는 것이 맞다!'''
            for i in range(1, len(board1d)):
                if num == board1d[i]:
                    cnt += 1
                elif cnt >= 4:
                    for j in range(sidx, i):
                        board1d[j] = 0
                    cnt_list[num] += cnt
                    sidx = i
                    num = board1d[sidx]
                    cnt = 1
                    fflag = True
                elif i == len(board1d) - 1:
                    if cnt >= 4:
                        for j in range(sidx, i):
                            board1d[j] = 0
                        cnt_list[num] += cnt
                        sidx = i
                        num = board1d[sidx]
                        cnt = 1
                        fflag = True
                else:
                    cnt = 1
                    sidx = i
                    num = board1d[sidx]
            # 이동 후 폭발가능하면 폭발하기 반복
            # print(f"\n{c}. expload | cnt_list: {cnt_list}")
            move_biz()
        # print('after_expload_board1d: ', board1d)
        # show(board1d)
        # // 구슬 변화하기
        temp_board = [0] * (n*n - 1)
        tidx = 0
        num = board1d[0]
        cnt = 1
        for i in range(1, len(board1d)):
            if num == board1d[i]:
                cnt += 1
            else:
                if tidx >= n*n - 1: break
                temp_board[tidx] = cnt
                if tidx + 1 >= n*n - 1: break
                temp_board[tidx + 1] = num
                num = board1d[i]
                cnt = 1
                tidx += 2
        for i in range(len(board1d)):
            board1d[i] = temp_board[i]
        # print('after_change_board1d: ', board1d)
        # print(f"{t}. board1d: ", board1d, "\n")
        # show(board1d)
    ans = 0
    for i in range(1, 4):
        ans += i * cnt_list[i]
    print(ans)

'''
느낀점
1. [문제잘읽자!] 문제를 잘 읽자 (폭발한 구슬의 갯수이니까 폭발한거만 cnt_list에 넣기)
2. [리스트이동문제] move_biz(); 동일 리스트안에서 이동이 발생할 경우 별도의 리스트둬서 copy하자
3. [초기값문제] 폭발하기에서 num을 board1d[0]으로이미 초기화했으니까 [1 ~ len(board1d)-1]까지 탐색하면됨 
4. [코드작성 순서문제] sidx = i; num = board1d[sidx]하기전에 cnt_list[num] += cnt 하자!
                        
'''
