# 20:20
def show(b):
    for i in range(r):
        for j in range(c):
            print(b[i][j], end = ' ')
        print()

def OOB(x, y):
    return x < 0 or x >= r or y < 0 or y >= c

def reduce():
    global board
    for i in range(0, 1):
        for j in range(1, c-1):
            if board[i][j] > 0:
                board[i][j] -= 1
    for i in range(r-1, r):
        for j in range(1, c-1):
            if board[i][j] > 0:
                board[i][j] -= 1
    for j in range(0, 1):
        for i in range(r):
            if board[i][j] > 0:
                board[i][j] -= 1
    for j in range(c-1, c):
        for i in range(r):
            if board[i][j] > 0:
                board[i][j] -= 1


def control():
    global board
    tboard = [[0 for _ in range(c)] for _ in range(r)]
    visited = [[False for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if OOB(nx, ny): continue
                if d == 0:
                    xx, yy = 0, 0
                    ch = 1
                elif d == 1:
                    xx, yy = 0, -1
                    ch = 1
                elif d == 2:
                    xx, yy = 0, 0
                    ch = 0
                elif d == 3:
                    xx, yy = 1, 0
                    ch = 0
                if ch in wall_board[x + xx][y + yy]: continue
                visited[x][y] = True
                if not visited[nx][ny] and board[nx][ny] > board[x][y]:
                    val = board[nx][ny] - board[x][y]
                    tboard[nx][ny] -= val//4
                    tboard[x][y] += val//4
                elif not visited[nx][ny] and board[nx][ny] < board[x][y]:
                    val = board[x][y] - board[nx][ny]
                    tboard[x][y] -= val//4
                    tboard[nx][ny] += val//4

    for i in range(r):
        for j in range(c):
            board[i][j] += tboard[i][j]



def spread(x, y, d):
    global board, wall_board
    if d == 0:
        ld, rd = 2, 3
        xy = [-1, 1, 0, 1, 1, 1]
        ww = [0, 0, -1, 0, 0, 0, 1, 0, 1, 0]
        c1, c2 = 0, 1
    elif d == 1:
        ld, rd = 3, 2
        xy = [1, -1, 0, -1, -1, -1]
        ww = [1, 0, 1, -1, 0, -1, 0, 0, -1, -1]
        c1, c2 = 0, 1
    elif d == 2:
        ld, rd = 1, 0
        xy = [-1, -1, -1, 0, -1, 1]
        ww = [0, -1, 0, -1, 0, 0, 0, 0, 0, 1]
        c1, c2 = 1, 0
    elif d == 3:
        ld, rd = 0, 1
        xy = [1, 1, 1, 0, 1, -1]
        ww = [0, 0, 1, 1, 1, 0, 0, -1, 1, -1]
        c1, c2 = 1, 0
    '''그림 4, 5, 6, 7, 8 통과'''
    amount = 5
    nx, ny = x + dx[d], y + dy[d] # 5 = 온풍기
    temp_board = [[0 for _ in range(c)] for _ in range(r)]
    temp_board[nx][ny] = amount # 5
    step = 1
    while amount > 1:
        step += 1
        amount -= 1
        origin_x, origin_y = nx, ny
        # left
        for i in range(1, step):
            nnx, nny = nx + xy[2], ny + xy[3]
            if OOB(nnx, nny): break
            if temp_board[nx][ny] != 0 and c2 not in wall_board[nx + ww[4]][ny + ww[5]]:
                temp_board[nnx][nny] = amount
            rx, ry = nx + xy[4], ny + xy[5]
            if not OOB(rx, ry) and temp_board[nx][ny] != 0 and c1 not in wall_board[nx + ww[6]][ny + ww[7]] and \
                    c2 not in wall_board[nx + ww[8]][ny + ww[9]]:
                temp_board[rx][ry] = amount
            lx, ly = nx + xy[0], ny + xy[1]
            if not OOB(lx, ly) and temp_board[nx][ny] != 0 and c1 not in wall_board[nx + ww[0]][ny + ww[1]] and \
                    c2 not in wall_board[nx + ww[2]][ny + ww[3]]:
                temp_board[lx][ly] = amount

            nx, ny = nx + dx[ld], ny + dy[ld] # left로 한칸 전진
            if OOB(nx, ny): break

        # right
        nx, ny = origin_x, origin_y
        for i in range(1, step):
            nnx, nny = nx + xy[2], ny + xy[3]
            if OOB(nnx, nny): break
            if temp_board[nx][ny] != 0 and c2 not in wall_board[nx + ww[4]][ny + ww[5]]:
                temp_board[nnx][nny] = amount
            lx, ly = nx + xy[0], ny + xy[1]
            if not OOB(lx, ly) and temp_board[nx][ny] != 0 and c1 not in wall_board[nx + ww[0]][ny + ww[1]] and \
                    c2 not in wall_board[nx + ww[2]][ny + ww[3]]:
                temp_board[lx][ly] = amount
            rx, ry = nx + xy[4] , ny + xy[5]
            if not OOB(rx, ry) and temp_board[nx][ny] != 0 and c1 not in wall_board[nx + ww[6]][ny + ww[7]] and \
                    c2 not in wall_board[nx + ww[8]][ny + ww[9]]:
                temp_board[rx][ry] = amount

            nx, ny = nx + dx[rd], ny + dy[rd] # right로 한칸 전진
        nx, ny = origin_x + dx[d], origin_y + dy[d]

    for i in range(r):
        for j in range(c):
            board[i][j] += temp_board[i][j]

def check_again():
    global k, board
    for ch in ch_loc:
        if board[ch[0]][ch[1]] < k:
            return True
    return False

if __name__ == "__main__":
    r, c, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]
    w = int(input())
    wall_loc = [list(map(int, input().split())) for _ in range(w)]
    wall_board = [[[] for _ in range(c)] for _ in range(r)]
    for w in wall_loc:
        wall_board[w[0]-1][w[1]-1].append(w[2])

    on_loc = []
    ch_loc = []
    # 0-e, 1-w 2-n 3-s
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    ans = 0 # chocolat cnt
    # 온풍기, 온도체크할 위치 할당
    for i in range(r):
        for j in range(c):
            if 1 <= board[i][j] <= 4:
                on_loc.append([i, j, board[i][j]-1])
                board[i][j] = 0
            elif board[i][j] == 5:
                ch_loc.append([i, j])
                board[i][j] = 0
    flag = True
    while flag:
        # 1. 온풍기에서 바람나옴
        for on in on_loc:
            on_r, on_c, on_d = on[0], on[1], on[2]
            spread(on_r, on_c, on_d)
        # 2. 온도조절
        control()
        # 3. 바깥쪽 1도 감소
        reduce()
        # 4. 초콜릿 하나 먹음
        ans += 1
        if ans > 100: break
        # 5. 조사하는 칸 k이상 인지 확인
        flag = check_again()

    print(ans)

'''
<느낀점>
1. 문제에서 제시한 방법대로 그대로 풀자! -> 내 방식대로 생각해서 풀다가 꼬일 수 있다!
2. 규칙 정할 때 실수 없이 꼼꼼하게 정하자!
3. 함수구현후 유닛테스트 꼭 돌려보자(control에서 visited[][]필요한지 확인할 수 있음)
'''
