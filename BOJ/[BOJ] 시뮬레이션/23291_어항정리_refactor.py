def OOB(x, y):
    return x < 0 or x >=n or y < 0 or y >= n

# 최소 물고기 수 가진 어항에 1마리씩 
def addOne(board):
    min_val = board[0][0]
    for i in range(1, n):
        if min_val > board[i][0]:
            min_val = board[i][0]
    for i in range(n):
        if min_val == board[i][0]:
            board[i][0] += 1
    return board

# 바닥에 있는 어항 중(board[i][0] 중)에 최조로 0이 아닌 idx 리턴
def findVidx(board):
    vidx = 0
    for i in range(n):
        if board[i][0] != 0:
            vidx = i; break
    return vidx
# idx 번째 행에 있는 어항 중에 다음 어항이 쌓일 위치 리턴
def findHidx(idx):
    hidx = 1
    if board[idx][0] == 0: return -1
    for i in range(n):
        if board[idx][i] == 0:
            hidx = i; break
    return hidx
  
# 90도 회전
def turn90(bboard, row, col):
    tboard = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            tboard[i][j] = bboard[i][j]
    rboard = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(col):
        for j in range(row):
            rboard[i][j] = tboard[row-1-j][i]
    return rboard

# 공중부양 후 90도 회전해서 어항쌓기
def flyTurn90(board):
    idx = 0
    while True:
        if idx == 0:
            temp = board[0][0]
            board[0][0] = 0
            board[1][1] = temp
            idx += 1
        elif idx == 1:
            temp1 = board[1][0]
            temp2 = board[1][1]
            board[1][0] = 0
            board[1][1] = 0
            board[2][1] = temp1
            board[3][1] = temp2
            idx += 1
        else:
            vidx = findVidx(board)
            hidx = findHidx(vidx)
            endIdx = 2147000000
            for i in range(vidx, n):
                if board[i][hidx-1] == 0:
                    endIdx = i; break
            # turn90 했을 때 바닥에 어항이 없는 경우
            if hidx > n-endIdx: break

            origin_row, origin_col = endIdx-vidx, hidx
            temp_board = []
            for i in range(vidx, endIdx):
                temp_board.append(board[i][:])
            for i in range(vidx, endIdx):
                for j in range(hidx):
                    board[i][j] = 0
            # 90도 회전
            temp_board = turn90(temp_board, origin_row, origin_col)
            new_row, new_col = origin_col, origin_row
            for i in range(new_row):
                for j in  range(new_col):
                    board[vidx+origin_row+i][j+1] = temp_board[i][j]
    return board
  
# 물고기 수 조정하기
def adjustFishBowl(board):
    temp_board = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0: continue
            for d in range(4):
                nx, ny = x + dx[d], y +dy[d]
                if OOB(nx, ny): continue
                if board[nx][ny] == 0: continue
                if board[nx][ny] > board[x][y]:
                    val = board[nx][ny] - board[x][y]
                    temp_board[nx][ny] -= val//5
                    temp_board[x][y] += val//5
    for x in range(n):
        for y in range(n):
            board[x][y] += temp_board[x][y]
    return board

# 모두 바닥에 내려놓기
def makeOneRow(board):
    insert_idx = 0
    temp_board = [[0 for _ in range(n)] for _ in range(n)]
    vidx = findVidx(board)
    while insert_idx < n:
        for i in range(len(board[vidx])):
            if board[vidx][i] == 0: break
            temp_board[insert_idx][0] = board[vidx][i]
            insert_idx += 1
        vidx += 1
    return temp_board

# 공중부양 후 180도 회전
def flyTurn180(board):
    insert_idx = n-1
    for i in range(n//2):
        board[insert_idx - i][1] = board[i][0]
        board[i][0] = 0
    idx = 0
    for i in range(n//2+n//4-1, n//2-1, -1):
        board[n//2+n//4 + idx][2] = board[i][1]
        board[n//2+n//4 + idx][3] = board[i][0]
        board[i][1] = 0
        board[i][0] = 0
        idx += 1
    return board
  
# 어항의 물고기 수의 최대와 최소의 차이가 k이하 인지/아닌지 -> T/F
def checkCondition(board, k):
    min_val, max_val = 2147000000, -2147000000
    for i in range(n):
        if min_val > board[i][0]:
            min_val = board[i][0]
        if max_val < board[i][0]:
            max_val = board[i][0]
    return (max_val - min_val <= k)

if __name__ == "__main__":
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n, k = map(int, input().split())
    # 어항의 바닥을 각 행의 0번째 열로 두고, 어항이 쌓이는 걸 열의 index로 관리함
    board = [[0 for _ in range(n)] for _ in range(n)]
    temp = list(map(int, input().split()))
    for i in range(n):
        board[i][0] = temp[i]
    ans = 0
    while True:
        ans += 1
        # 1. 최소 물고기 수 가진 어항에 1마리 채워주기
        board = addOne(board)
        # 2. 공중부양 후 시계 방향으로 90도 회전
        board = flyTurn90(board)
        # 3. 물고기 수 조절
        board = adjustFishBowl(board)
        # 4. 일렬 배치
        board = makeOneRow(board)
        # 5. 공중 부양 후 180도 회전
        board = flyTurn180(board)
        # 6. 물고기 수 조절
        board = adjustFishBowl(board)
        # 7. 일렬 배치
        board = makeOneRow(board)
        # 8. 반복조건 체크
        if checkCondition(board, k):
            print(ans)
            break
'''
느낀점
1. 기능 별로 테스트 해본 거 good
2. turn90()에서 가로,세로 길이를 고정하는게 아니라 좌표값을 구해서 각 사이즈에 맞게 rboard[][]리스트 생성하자!
새로 회전시켜서 놓았을 때 바닥에 어항이 있는지 확인하는 방식으로 접근하자!
3. n=4일 때, flyTurn90() 하게 되면
0 0 0 0 
0 0 0 0 
0 0 0 0 
4000 4400 5602 6002 
이렇게된다!
5. flyTurn90()에서 n=4일때와 n이 4보다 클때 규칙을 찾아서 잘 break를 설정해야된다!
'''
