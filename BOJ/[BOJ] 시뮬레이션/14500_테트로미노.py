# 1635 1830
def OOB(i, j):
    global N, M
    return i < 0 or i >= N or j < 0 or j >= M

def put_tt(x, y, dir):
    global board
    sum_val = 0
    if dir == 0:
        if not OOB(x, y+3):
            for i in range(y, y+4):
               sum_val += board[x][i]
    elif dir == 1:
        if not OOB(x+3, y):
            for i in range(x, x+4):
                sum_val += board[i][y]
    elif dir == 2:
        if not OOB(x+1, y+1):
            sum_val = board[x][y] + board[x+1][y] + board[x][y+1] + board[x+1][y+1]
    elif dir == 3:
        if not OOB(x+2, y+1):
            for i in range(x, x+3):
                if i == x+2:
                    sum_val += board[i][y+1]
                sum_val += board[i][y]
    elif dir == 4:
        if not OOB(x+2, y+1):
            for i in range(x, x+3):
                if i == x:
                    sum_val += board[i][y+1]
                sum_val += board[i][y]
    elif dir == 5:
        if not OOB(x+2, y+1):
            for i in range(x, x+3):
                if i == x:
                    sum_val += board[i][y]
                sum_val += board[i][y+1]
    elif dir == 6:
        if not OOB(x+1, y+2):
            for i in range(y, y+3):
                if i == y:
                    sum_val += board[x][i]
                sum_val += board[x+1][i]
    elif dir == 7:
        if not OOB(x+1, y+2):
            for i in range(y, y+3):
                if i == y+2:
                    sum_val += board[x][i]
                sum_val += board[x+1][i]
    elif dir == 8:
        if not OOB(x+2, y+1):
            for i in range(x, x+3):
                if i == x+2:
                    sum_val += board[i][y]
                sum_val += board[i][y+1]
    elif dir == 9:
        if not OOB(x+1, y+2):
            for i in range(y, y+3):
                if i == y+2:
                    sum_val += board[x+1][i]
                sum_val += board[x][i]
    elif dir == 10:
        if not OOB(x+1, y+2):
            for i in range(y, y+3):
                if i == y:
                    sum_val += board[x+1][i]
                sum_val += board[x][i]
    elif dir == 11:
        if not OOB(x+2, y+1):
            sum_val = board[x][y] + board[x+1][y] + board[x+1][y+1] + board[x+2][y+1]
    elif dir == 12:
        if not OOB(x+1, y+2):
            sum_val = board[x][y] + board[x][y+1] + board[x+1][y+1] + board[x+1][y+2]
    elif dir == 13:
        if not OOB(x+1, y+2):
            sum_val = board[x+1][y] + board[x+1][y+1] + board[x][y+1] + board[x][y+2]
    elif dir == 14:
        if not OOB(x+2, y+1):
            sum_val = board[x][y+1] + board[x+1][y+1] + board[x+1][y] + board[x+2][y]
    elif dir == 15:
        if not OOB(x+1, y+2):
            for i in range(y, y+3):
                if i == y+1:
                    sum_val += board[x+1][i]
                sum_val += board[x][i]
    elif dir == 16:
        if not OOB(x+1, y+2):
            for i in range(y, y+3):
                if i == y+1:
                    sum_val += board[x][i]
                sum_val += board[x+1][i]
    elif dir == 17:
        if not OOB(x+2, y+1):
            for i in range(x, x+3):
                if i == x+1:
                    sum_val += board[i][y+1]
                sum_val += board[i][y]
    elif dir == 18:
        if not OOB(x+2, y+1):
            for i in range(x, x+3):
                if i == x+1:
                    sum_val += board[i][y]
                sum_val += board[i][y+1]
    return sum_val


if __name__ == "__main__":
    N, M = map(int, input().split())
    # dir [0~1]-??????, [2]-??????, [3~10]-??????, [11~14]-??????, [15~18]-??????
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    max_val = 0
    for i in range(N):
        for j in range(M):
            for k in range(19):
                max_val = max(max_val, put_tt(i,j,k))
    print(max_val)
'''
?????????
1. N, M??? ?????? 500 ?????? ???????????? ??? ????????? ????????? ??? k=19?????? ???????????? ????????? 
????????? k = 20????????? ??????
N x M x k = 250,000 x 20 = 5,000,000 = 5 x 10^6 ?????? ?????????
3??? for????????? ???????????? ???.
2. ?????? ????????? ???????????? ????????? ?????? ????????? ?????? ????????? ?????? ???????????? ????????? ???????????? ?????? ?????????.
????????? ????????? ????????? dir ????????? ?????? ???????????? ????????? ???
'''