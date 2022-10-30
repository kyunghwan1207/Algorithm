def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def count_satis(x, y, lis):
    res = 0
    for d in range(4):
        nx, ny =  x + dx[d], y + dy[d]
        if OOB(nx, ny): continue
        if board[nx][ny] in lis:
            res += 1
    return res

def count_empty(x, y):
    res = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if OOB(nx, ny): continue
        if board[nx][ny] == 0:
            res += 1
    return res

def sit(board):
    global like_list
    for like in like_list:
        a, b, c, d, e = like
        max_val = -1
        max_ecnt = -1
        max_pos = []
        for i in range(n):
            for j in range(n):
                if board[i][j] != 0: continue
                val = count_satis(i, j, [b, c, d, e])
                ecnt = count_empty(i, j)
                if max_val <= val:
                    if max_val == val:
                        if max_ecnt < ecnt:
                            max_val = val
                            max_ecnt = ecnt
                            max_pos = [i, j]
                        else: pass
                    else:
                        max_val = val
                        max_ecnt = ecnt
                        max_pos = [i, j]
        board[max_pos[0]][max_pos[1]] = a
    return board

def getSatisDegree(board):
    global like_list
    res = 0
    for i in range(n):
        for j in range(n):
            p = board[i][j]
            cnt = 0
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if OOB(nx, ny): continue
                if board[nx][ny] in llist[p]:
                    cnt += 1
            res += getVal(cnt)
    return res

def getVal(cnt):
    if cnt < 2:
        return cnt
    else:
        return 10**(cnt-1)

if __name__ == "__main__":
    n = int(input())
    nn = n**2
    like_list = []
    llist = [0]*(n**2+1)
    board = [[0]*n for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(nn):
        a, b, c, d, e = map(int, input().split())
        like_list.append([a, b, c, d, e])
        llist[a] = [b, c, d, e]
    board = sit(board)

    print(getSatisDegree(board))
