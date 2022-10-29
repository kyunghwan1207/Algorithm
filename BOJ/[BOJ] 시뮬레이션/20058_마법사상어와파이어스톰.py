def OOB(x, y):
    return x < 0 or x >= (1<<n) or y < 0 or y >= (1<<n)

def turn90(x, y, nn):
    global board
    temp_board = [[0]*nn for _ in range(nn)]
    for j in range(y, y+nn):
        for i in range(x+nn-1, x-1, -1):
            temp_board[j-y][x+nn-1 - i] = board[i][j]
    for i in range(x, x+nn):
        for j in range(y, y+nn):
            board[i][j] = temp_board[i-x][j-y]

def check(x, y):
    cnt = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if not OOB(nx, ny) and board[nx][ny] > 0:
            cnt += 1
    return cnt >= 3

def decrease():
    temp_board = [[0]*(1<<n) for _ in range(1<<n)]

    for i in range(1<<n):
        for j in range(1<<n):
            if board[i][j] == 0: continue
            if not check(i, j):
                temp_board[i][j] -= 1
    for i in range(1<<n):
        for j in range(1<<n):
            board[i][j] += temp_board[i][j]

def bfs(x, y):
    global visited
    q = []
    q.append([x, y])
    idx = 0
    count = 1
    visited[x][y] = True
    while len(q) > idx:
        x, y = q[idx]
        idx += 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if OOB(nx, ny): continue
            if not visited[nx][ny] and board[nx][ny] > 0:
                q.append([nx, ny])
                visited[nx][ny] = True
                count += 1

    return count

if __name__ == "__main__":
    n, Q = map(int, input().split())
    board = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for _ in range(1<<n):
        board.append(list(map(int, input().split())))
    Q_list = list(map(int, input().split()))
    for i in range(Q):
        L = Q_list[i]
        nn = 1<<L
        for i in range(0, 1<<n, nn):
            for j in range(0, 1<<n, nn):
                turn90(i, j, nn)
        decrease()

    amount = 0
    for i in range(1<<n):
        for j in range(1<<n):
            amount += board[i][j]
    max_val = 0
    visited = [[False]*(1<<n) for _ in range(1<<n)]
    for i in range(1<<n):
        for j in range(1<<n):
            if not visited[i][j] and board[i][j] > 0:
                val = bfs(i, j)
                if max_val < val:
                    max_val = val

    print(amount)
    print(max_val)
'''
느낀점
1. board[][] 얼음이 음수되지 않게 decrse()잘하자!
2. turn90()에서 temp_board[][]를 nn크기(2**L) 만큼만 잡았기 때문에
board[][]에서 들어오는 좌표가 커지더라도 인덱스를 temp_board[][]크기안에 둘 수 있게
조정하는 작업(i-x, j-y)등이 필요했다.
3. bfs()에서 얼음덩어리 체크할 때 방문한 횟수로 체크하자!
bfs() param으로 cnt넣는것은? 안된다!
'''
