from collections import deque
'''
선택된 학생들이 자리에 앉은 모습을 출력 하는 함수
'''
def printBoard(girlPos):
    global board
    tempBoard = [['.' for _ in range(5)] for _ in range(5)]
    for pos in girlPos:
        x, y = pos//5, pos%5
        tempBoard[x][y] = board[x][y]
    for i in range(5):
        for j in range(5):
            print(tempBoard[i][j], end=' ')
        print()
    print()

'''
격자 범위를 벗어났는지 check하는 함수
'''
def OOB(x, y):
    return x < 0 or x >= 5 or y < 0 or y >= 5
'''
7명이 인접해있고, 이다솜파 학생이 4명이상 포함되었는지 확인하는 함수 = BFS 알고리즘 사용
'''
def isSevenPrincess(girlPos):
    global board
    visited = [[False] * 5 for _ in range(5)]
    x, y = girlPos[0] // 5, girlPos[0] % 5
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    connectCnt = 1 # 인접한 학생 수
    sCnt = 1 if board[x][y] == 'S' else 0  # 이다솜파 학생 수

    q = deque()
    q.append([x, y])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if OOB(nx, ny) or visited[nx][ny]:
                continue
            nextPos = nx*5 + ny
            if nextPos in girlPos:
                visited[nx][ny] = True
                if board[nx][ny] == 'S':
                    sCnt += 1
                q.append([nx, ny])
                connectCnt += 1
    return (connectCnt == 7 and sCnt >= 4)

'''
학생들을 선택할 수 있는 모든 경우의 수 = 25_C_7
'''
def getAllCase(girlPos, startIdx, ycnt):
    global ans
    if len(girlPos) == 7:
        if isSevenPrincess(girlPos):
            # printBoard(girlPos)
            ans += 1
        return
    if ycnt >= 4: # 임도현파 학생이 4명이상일 경우엔 더이상 볼 필요x
        return
    # prev = -1
    for i in range(startIdx, 25):
        # if i not in girlPos and i != prev: # 0~24 중엔 충복 되는 수가 없기 때문에 필요x
        #     prev = i
        x, y = i//5, i%5
        if board[x][y] == 'S':
            girlPos.append(i)
            getAllCase(girlPos, i+1, ycnt)
            girlPos.pop()
        else:
            girlPos.append(i)
            getAllCase(girlPos, i+1, ycnt + 1)
            girlPos.pop()


if __name__ == "__main__":
    board = [[g for g in input()] for _ in range(5)]
    girlPos, startIdx, ycnt = [], 0, 0
    ans = 0 # 문제에서 요구하는 모든 경우의 수
    getAllCase(girlPos, startIdx, ycnt)
    print(ans)


'''
1. DFS는 특성상 십자모양으로 갈라지는 탐색을 하긴 어렵다. 그래서 BT로 모든 경우를 고려해야함
2. 0~24 숫자를 7개 선택하는 것으로 볼 수 있다. 각 숫자를 5*5 좌표로 변환하면 됨
=> i: 0 ~ 24까지 x = i//5, y = i%5 를 통해서 (x, y)좌표 구할 수 있음
=> 25_C_7 로 구할 수 있음(선택하는 순서가 결과에 영향을 주지 않는다. 즉, 순서 상관 없기 때문)
3. 7개 선택 후 인접 인원 수와 이다솜파 학생 수를 체크하는 것 필요
'''