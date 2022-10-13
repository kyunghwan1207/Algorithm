def show(b):
    for i in range(r):
        for j in range(c):
            print(b[i][j], end = ' ')
        print()

def OOB(x, y):
    return x < 0 or x >= r or y < 0 or y >= c

def check_right(x, y):
    if OOB(x, y): return False
    if wall_right[x][y] == 1: return False
    nx, ny = x + dx[0], y + dy[0]
    if OOB(nx, ny): return False
    return True

def check_left(x, y):
    if OOB(x, y): return False
    nx, ny = x + dx[1], y + dy[1]
    if OOB(nx, ny): return False
    if wall_right[nx][ny] == 1: return False
    return True

def check_up(x, y):
    if OOB(x, y): return False
    if wall_up[x][y] == 0: return False
    nx, ny = x + dx[2], y + dy[2]
    if OOB(nx, ny): return False
    return True

def check_down(x, y):
    if OOB(x, y): return False
    nx, ny = x + dx[3], y + dy[3]
    if OOB(nx, ny): return False
    if wall_up[nx][ny] == 0: return False
    return True


def spread(x, y, d):
    global board
    # 온풍기 위치: (x, y)
    temp = [[0 for _ in range(c)] for _ in range(r)]
    nx, ny = x + dx[d], y + dy[d]
    if OOB(nx, ny): return temp
    temp[nx][ny] = 5
    q = []
    q.append([nx, ny, 5])
    idx = 0
    while len(q) > idx:
        nx, ny, amount = q[idx][0], q[idx][1], q[idx][2]
        idx += 1
        if amount <= 0: break
        # east
        if d == 0:
            if check_up(nx, ny):
                if check_right(nx-1, ny):
                    temp[nx-1][ny+1] = amount-1
                    q.append([nx - 1, ny + 1, amount-1])
            if check_right(nx, ny):
                temp[nx][ny+1] = amount-1
                q.append([nx, ny+1, amount-1])
            if check_down(nx, ny):
                if check_right(nx+1, ny):
                    temp[nx+1][ny+1] = amount-1
                    q.append([nx+1, ny+1, amount-1])
        # west
        elif d == 1:
            if check_up(nx, ny):
                if check_left(nx-1, ny):
                    temp[nx-1][ny-1] = amount-1
                    q.append([nx-1, ny-1, amount-1])
            if check_left(nx, ny):
                temp[nx][ny-1] = amount-1
                q.append([nx, ny-1, amount-1])
            if check_down(nx, ny):
                if check_left(nx+1, ny):
                    temp[nx+1][ny-1] = amount-1
                    q.append([nx+1, ny-1, amount-1])
        # north
        elif d == 2:
            if check_right(nx, ny):
                if check_up(nx, ny+1):
                    temp[nx-1][ny+1] = amount-1
                    q.append([nx-1, ny+1, amount-1])
            if check_up(nx, ny):
                temp[nx-1][ny] = amount-1
                q.append([nx-1, ny, amount-1])
            if check_left(nx, ny):
                if check_up(nx, ny-1):
                    temp[nx-1][ny-1] = amount-1
                    q.append([nx-1, ny-1, amount-1])
        # south
        elif d == 3:
            if check_left(nx, ny):
                if check_down(nx, ny-1):
                    temp[nx+1][ny-1] = amount-1
                    q.append([nx+1, ny-1, amount-1])
            if check_down(nx, ny):
                temp[nx+1][ny] = amount-1
                q.append([nx+1, ny, amount-1])
            if check_right(nx, ny):
                if check_down(nx, ny+1):
                    temp[nx+1][ny+1] = amount-1
                    q.append([nx+1, ny+1, amount-1])
    return temp

def blow():
    global board, heater_loc, r, c
    for heater in heater_loc:
        x, y, d = heater[0], heater[1], heater[2]
        # call function
        tboard = spread(x, y, d)
        for i in range(r):
            for j in range(c):
                board[i][j] += tboard[i][j]
# 온도 조절
def adjust():
    global board
    temp = [[0 for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if OOB(nx, ny): continue
                if board[nx][ny] > board[x][y]:
                    flag = False
                    if d == 0 and check_right(x, y): flag = True
                    elif d == 1 and check_left(x, y): flag = True
                    elif d == 2 and check_up(x, y): flag = True
                    elif d == 3 and check_down(x, y): flag = True
                    if flag:
                        val = board[nx][ny] - board[x][y]
                        temp[nx][ny] -= val // 4
                        temp[x][y] += val // 4
    for i in range(r):
        for j in range(c):
            board[i][j] += temp[i][j]

# 맨 바깥쪽 온도 1씩 감소
def decrease():
    global board
    for x in range(1, r-1):
        if board[x][0] > 0: board[x][0] -= 1
        if board[x][c-1] > 0: board[x][c-1] -= 1
    for y in range(0, c):
        if board[0][y] > 0: board[0][y] -= 1
        if board[r-1][y] > 0: board[r-1][y] -= 1

# check_loc에 있는 칸의 온도가 모두 k이상인지 확인
def check():
    for c in check_loc:
        x, y = c[0], c[1]
        if board[x][y] < k:
            return True
    return False

if __name__ == "__main__":
    r, c, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]
    w = int(input())
    wall_up = [[2 for _ in range(c)] for _ in range(r)] # 위 벽
    wall_right = [[2 for _ in range(c)] for _ in range(r)] # 오른쪽 벽
    heater_loc = []
    check_loc = []
    #    e   w   n  s
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for _ in range(w):
        wx, wy, ww = map(int, input().split())
        # wall_board[wx-1][wy-1] = ww
        if ww == 0:
            wall_up[wx - 1][wy - 1] = 0 # 위 벽
        else:
            wall_right[wx - 1][wy - 1] = 1 # 오른쪽 벽

    for i in range(r):
        for j in range(c):
            if board[i][j] == 0: continue
            elif 1 <= board[i][j] <= 4:
                heater_loc.append([i, j, board[i][j] - 1])
                board[i][j] = 0
            elif board[i][j] == 5:
                check_loc.append([i, j])
                board[i][j] = 0
    ans = 0 # 초콜릿 갯수
    flag = True
    while flag:
        flag = False
        # # 1. 온풍기에서 바람나옴
        blow()
        # 2. 온도 조정
        adjust()
        # 3. 바깥쪽 온도 감소
        decrease()
        ans += 1
        if ans > 100: break
        # 4. check_loc에 있는 칸 온도가 모두 k 이상 인지 확인
        flag = check()
    print(ans)



'''
<느낀점>
1. 문제에서 제시한 방법대로 그대로 풀자! -> 내 방식대로 생각해서 풀다가 꼬일 수 있다!
2. 규칙 정할 때 실수 없이 꼼꼼하게 정하자!
3. 함수구현후 유닛테스트 꼭 돌려보자(control에서 visited[][]필요한지 확인할 수 있음)
4. 작은 기능이더라도 복잡 or 반복사용 된다면 무조건 함수로 만들어서 관리하자! (check_up, check_right ...)
5. 초기화할 때 영향에 미치는 값을 생각해서 잘 하자 wall_board는 초기값이 0이면 안된다!
6. **초기화할 때 벽정보가 겹치는 칸에 들어올 수 있으니까 위벽, 오른쪽벽 입력받는것을 따로둬야한다!**
7. adjust()함수에서 방문체크보다 문제에서 제시한 것 처럼 큰 값에서 작은값으로 값이 이동한다에만 신경쓰자!
(어차피 작은값일때 큰값과 비교될 때 조건문 충족못하므로 겹치지 않을 것임.)
'''
