# 22:33~24:33
# import sys
# sys.stdin = open("../input.txt", "r")
def OOB(r, c):
    global R, C
    return r < 0 or r >= R or c < 0 or c >= C
def show_board(board):
    global R, C
    for i in range(R):
        print()
        for j in range(C):
            print(board[i][j], end = ' ')
    print()
    return

def spread():
    global R, C, board, dr, dc, cleaner
    board2 = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            board2[i][j] = board[i][j]
    cnt = 0
    spread_lis = []
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                # print(f'i:{i}, j:{j}, A_r,c: {board[i][j]}')
                r, c = i, j
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not OOB(nr, nc) and board[nr][nc] != -1:
                        cnt += 1
                        if cnt == 1:
                            spread_lis.append([r, c, cnt, []])
                            spread_lis[-1][3].append([nr, nc])
                        else:
                            spread_lis[-1][2] += 1
                            spread_lis[-1][3].append([nr, nc])
                        # spread_lis.append([nr, nc])
                        # print(f'd:{d}. r:{r}, c: {c}, nr: {nr}, nc: {nc}, A_rc: {board[r][c]}, B_rc: {board2[nr][nc]}')
                if cnt > 0:
                    board2[r][c] = board[r][c] - (board[r][c] // 5) * cnt
                    # for lis in spread_lis:
                    #     board2[lis[0]][lis[1]] += board[r][c]//5
                # spread_lis = []
                cnt = 0
    # *old-version*
    # for i in range(R):
    #     for j in range(C):
    #         if board[i][j] > 0:
    #             r, c = i, j
    #             for d in range(4):
    #                 nr = r + dr[d]
    #                 nc = c + dc[d]
    #                 if not OOB(nr, nc) and board[nr][nc] != -1:
    #                     board2[nr][nc] += board[r][c] // 5

    # *new-version*
    # print('spread_lis: ', spread_lis)
    for lis in spread_lis: # 확산할 수 있는 좌표
        r, c, cnt, lis_temp = lis[0], lis[1], lis[2], lis[3]
        # print('lis_temp: ', lis_temp)
        for l in lis_temp: # 확산할 좌표
            board2[l[0]][l[1]] += board[r][c] // 5

    return board2

def work():
    global R, C,board, dr, dc, cleaner
    # up: cleaner[0][0], [0][1]
    # e n w s
    # 0 1 2 3
    # 바람방향이랑 거꾸로 오면서 한칸씩 바람방향으로 옮기기
    # n e s w
    r, c = cleaner[0][0], cleaner[0][1]
    # print('---up---')
    for d in range(1, 11, 3): # 1 4 7 10
        nd = d% 4 # 1 0 3 2
        nr, nc = r, c
        rd = (nd+2)%4 # 반대방향
        while 0 <= nr + dr[nd] <= cleaner[0][0] and 0 <= nc+dc[nd] <= C-1:
            nr += dr[nd]
            nc += dc[nd]
            nnr = nr + dr[rd]
            nnc = nc + dc[rd]
            if nnr > cleaner[0][0] or OOB(nnr, nnc): continue

            if nr == cleaner[0][0] and nc == cleaner[0][1]:
                break

            if board[nnr][nnc] == -1:
                board[nr][nc] = 0
            else:
                board[nnr][nnc] = board[nr][nc]
                board[nr][nc] = 0
        r, c = nr, nc


    # down: cleaner[1][0], [1][1]
    # e s w n
    # 0 3 2 1
    # 바람이랑 반대로
    # s e n w
    #print('---down---')
    r, c = cleaner[1][0], cleaner[1][1]
    for d in range(3, 7): # 3 4 5 6
        nd = d % 4
        nr, nc = r, c
        rd = (nd+2)%4
        while cleaner[1][0] <= nr+dr[nd] <= R-1 and 0 <= nc+dc[nd] <= C-1:
            nr += dr[nd]
            nc += dc[nd]
            nnr = nr + dr[rd]
            nnc = nc + dc[rd]
            if nnr < cleaner[1][0] or OOB(nnr, nnc): continue

            if nr == cleaner[1][0] and nc == cleaner[1][1]:
                break
            if board[nnr][nnc] == -1:
                board[nr][nc] = 0
            else:
                board[nnr][nnc] = board[nr][nc]
                board[nr][nc] = 0
        r, c = nr, nc


if __name__ == "__main__":
    R, C, T = map(int, input().split())
    board = []
    cleaner = [] # [[r1, c1], [r2, c2]]
    #     e  n   w   s
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    for _ in range(R):
        board.append(list(map(int, input().split())))
    for i in range(R): # 공기청정기는 0열에만 존재함
        if board[i][0] == -1:
            cleaner.append([i, 0])
            cleaner.append(([i+1, 0]))
            break
    for _ in range(T):
        board = spread()
        # show_board(board)
        work()
    res = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                res += board[i][j]
    print(res)


'''
느낀점
1. 반복문의 인자는 건드리지 말자!
ex. for d in range(4): d %= 4 (x) -> nd = d%4
2. 배열회전시킬때 범위를 잘 보자 무조건 OOB로 잡지 말 것!
ex. not OOB -> r <= cleaner[0][0] and c <= C-1 
3. 바람부는 방향에서 거꾸로 접근하는 것 좋았다 
+ 꺽이는 부분을 무조건신경쓰기 보단 꼭 신경써야하는가? 를 먼저 고민하고 코딩하자!
4. while문 안에서 nr += dr[d]를 하기 위해서 while조건에 nr + dr[d] 를 넣자
'''