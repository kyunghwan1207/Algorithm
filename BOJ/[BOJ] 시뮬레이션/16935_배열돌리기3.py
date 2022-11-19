import sys
input = sys.stdin.readline

def op1(n, m, p):
    global M
    M[-p] = [[0]*m for _ in range(n)]
    for i in range(n):
        M[-p][n-1-i] = M[p][i]
    return -p
def op2(n, m, p):
    global M
    M[-p] = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            M[-p][i][m-1-j] = M[p][i][j]
    return -p
def op3(n, m, p):
    global M
    M[-p] = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            M[-p][j][n-1-i] = M[p][i][j]
    return -p
def op4(n, m, p):
    global M
    M[-p] = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            M[-p][m-1-j][i] = M[p][i][j]
    return -p
def op5(n, m, p):
    global M
    M[-p] = [[0]*m for _ in range(n)]
    # 1 -> 2
    for i in range(n//2):
        for j in range(m//2):
            M[-p][i][m//2 + j] = M[p][i][j]
    # 2 -> 3
    for i in range(n//2):
        for j in range(m//2):
            M[-p][n//2 + i][m//2 + j] = M[p][i][m//2 + j]
    # 3 -> 4
    for i in range(n//2):
        for j in range(m//2):
            M[-p][n//2 + i][j] = M[p][n//2 + i][m//2 + j]
    # 4 -> 1
    for i in range(n//2):
        for j in range(m//2):
            M[-p][i][j] = M[p][n//2 + i][j]
    return -p
def op6(n, m, p):
    global M
    M[-p] = [[0]*m for _ in range(n)]
    # 1 -> 4
    for i in range(n//2):
        for j in range(m//2):
            M[-p][n//2 + i][j] = M[p][i][j]
    # 4 -> 3
    for i in range(n//2):
        for j in range(m//2):
            M[-p][n//2 + i][m//2 + j] = M[p][n//2 + i][j]
    # 3 -> 2
    for i in range(n//2):
        for j in range(m//2):
            M[-p][i][m//2 + j] = M[p][n//2 + i][m//2 + j]
    # 2 -> 1
    for i in range(n//2):
        for j in range(m//2):
            M[-p][i][j] = M[p][i][m//2 + j]
    return -p

n, m, r = map(int, input().split())
M = [[0], [], []] # M[1]: M1,  M[-1]: M2
for _ in range(n):
    M[1].append(list(map(int, input().split())))
command_list = list(map(int, input().split()))
# nxm 배열 두개 가지고 서로 왓다갓다하자
p = 1 # 연산을 가하는 행렬 -> M1
for i in range(len(command_list)): # r만큼 돈다
    if command_list[i] == 1:
        p = op1(n, m, p)
    elif command_list[i] == 2:
        p = op2(n, m, p)
    elif command_list[i] == 3:
        p = op3(n, m, p)
        n, m = len(M[p]), len(M[p][0])
    elif command_list[i] == 4:
        p = op4(n, m, p)
        n, m = len(M[p]), len(M[p][0])
    elif command_list[i] == 5:
        p = op5(n, m, p)
    elif command_list[i] == 6:
        p = op6(n, m, p)
for i in range(n):
    if i != 0:
        print()
    for j in range(m):
        print(M[p][i][j], end = ' ')
           
