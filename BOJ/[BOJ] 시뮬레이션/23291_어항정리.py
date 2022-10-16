def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

# 최소 물고기 수 가진 어항에 +1마리 추가
def fill():
    global board
    min_val = board[0][0]
    if min_val == 0: print(f"min_val: zero!!"); exit(0)
    for i in range(1, n):
        if min_val > board[i][0]:
            min_val = board[i][0]
    for i in range(n):
        if min_val == board[i][0]:
            board[i][0] += 1
          
# 공중부양 후 180도 회전
def fly_and_turn180():
    # n/2 -> n/2
    half_list = []
    for i in range(0, n//2):
        half_list.append(board[i][0])
        board[i][0] = 0
    k = 1
    for j in range(i+1, n):
        board[j][1] = half_list[-k]
        k+=1
    # n/2 -> n/4
    # 높이는 무조건 2
    first = [] # 그림-가로, 리스트-세로 기준
    second = []
    for j in range(i+1, i + 1 + n//4):
        first.append(board[j][0])
        second.append(board[j][1])
        board[j][0] = 0
        board[j][1] = 0
    idx = find_hidx(j+1)
    p = 1
    for k in range(j+1, n):
        board[k][idx]  = second[-p]
        board[k][idx+1] = first[-p]
        p += 1

# vidx: 리스트기준 세로로 처음 0이 아닌 위치
# hidx: 리스트 기준 가로로 처음 0인 위치
# 90도 회전
def turn90(vidx, hidx):
    # 리스트 모양에서 그대로 뗘오고 나서 회전시키자
    row = -1
    col = hidx
    for i in range(vidx, n):
        row += 1
        if board[i][hidx-1] == 0:
            break
    nrow, ncol = col, row # 3x4 = 4x3
    result = [[0 for _ in range(ncol)] for _ in range(nrow)] # 4 x 3
    for i in range(nrow):
        for j in range(ncol):
            # **어떤게 고정이고 어떤게 움직이는지 잘 보자**
            # row와 col이 바뀌었으니까 영향주는 것도 ncol, nrow이다!
            result[i][j] = board[vidx+ncol-1 - j][i]
            board[vidx+ncol-1 - j][i] = 0 # 움직이는 것이기 때문에 0으로 덮어쓰자

    for i in range(vidx+row, vidx+row+col):
        for j in range(len(result[0])):
            board[i][1+j] = result[i-vidx-row][j]
    return nrow, ncol

# 공중부양 후 90도 
def fly_and_turn90():
    idx = 0
    while True:
        if idx == 0:
            temp = board[0][0]
            board[1][1] = temp
            board[0][0] = 0
            idx += 1
        elif idx == 1:
            temp_list = board[1]
            for j in range(2):
                board[j+2][1] = temp_list[j]
                board[1][j] = 0
            idx += 1
            # **while 조건으로 두면 n이 커질 때 else로 가지 못하게 막아서
            # n=4일때만 잘 check해서 else로 가지 않게하면되기 때문에 여기서 break!**
            if n-idx <= idx: break
        else:
            idx = find_vidx()
            hidx = find_hidx(idx)
            nrow, ncol = turn90(idx, hidx)
            i = find_vidx()
            # 다음에 turn90()했을 때 어항바닥이 없다면 break
            if n - i - nrow < ncol+1: break

# board[i][0] 중에 처음으로 0이 아닌 vidx 찾아줌
def find_vidx():
    for i in range(n):
        if board[i][0] != 0:
            return i
    return 0

# row 주면 해당 row의 hidx 찾아줌
def find_hidx(row):
    for i in range(n):
        if board[row][i] == 0:
            return i
    return 0
  
# 인접한 어항에서 물고기 수 조정
def adjust():
    temp_board = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for d in range(4):
                if board[x][y] == 0: break
                nx, ny = x + dx[d], y + dy[d]
                if OOB(nx, ny): continue
                if board[nx][ny] == 0: continue
                if board[nx][ny] > board[x][y]:
                    val = board[nx][ny] - board[x][y]
                    temp_board[nx][ny] -= val // 5
                    temp_board[x][y] += val // 5

    for i in range(n):
        for j in range(n):
            board[i][j] += temp_board[i][j]
            
# 모든 어항을 바닥으로 내려 한줄로 정리
def arrange():
    # 채울 위치, 포인터
    sidx = 0
    for i in range(n):
        if board[i][0] != 0:
            pidx = i; break
    while pidx < n and sidx <= pidx:
        for i in range(len(board[pidx])):
            if board[pidx][i] == 0:
                pidx += 1; break
            board[sidx][0] = board[pidx][i]
            if i != 0:
                board[pidx][i] = 0
            sidx += 1
            
# 최대값, 최솟값 차이가 k이하인지 check
def check():
    max_val, min_val = -2147000000, 2147000000
    for i in range(n):
        if max_val < board[i][0]:
            max_val = board[i][0]
        if min_val > board[i][0]:
            min_val = board[i][0]
    return (max_val - min_val <= k)

if __name__ == "__main__":
    n, k = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(n)]
    lis = list(map(int, input().split()))
    #    e   s  w   n
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(n):
        board[i][0] = lis[i]
    ans = 0
    while True:
        ans += 1
        # 1. 최소 물고기 수 가진 어항에 1마리 채워주기 ++
        fill()
        # 2. 공중부양 후 90도 시계회전
        fly_and_turn90()
        # 3. 물고기 수 조절
        adjust()
        # a. 일렬 배치
        arrange()
        # 3. 공중부양후 180도 회전
        fly_and_turn180()
        # b. 물고기 조절
        adjust()
        # a. 일렬배치
        arrange()
        # 4. 반복조건 체크
        if check():
            break
    print(ans)

'''
느낀점
1. 기능 별로 테스트 해본 거 good
2. first, second 리스트 초기화는 배열 사용이후에 하자, ref값이 들어가기 때문에 사용전에 바꾸면 안됨!
3. turn90()에서 가로,세로 길이를 고정하는게 아니라 좌표값을 구해서 각 사이즈에 맞게 result[][]리스트 생성하자!
'''
