# 1420 ~ 1500 (실패 -> 성공(1530))

# 격자 범위에서 벗어나는지/아닌지 확인 -> T/F
def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= n
  
# 인접하는 칸에 존재하는 빈칸의 갯수
def get_blank_cnt(x, y):
    global board, n
    res = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if OOB(nx, ny): continue
        if board[nx][ny] == 0: res += 1
    return res
  
# 인접하는 칸에 존재하는 좋아하는 학생 수 구하기
def get_like_cnt(lis, x, y):
    global board
    res = 0
    for d in range(4):
        nx, ny = x + dx[d], y+ dy[d]
        if OOB(nx, ny): continue
        if board[nx][ny] in lis: res += 1
    return res

# 학생 배치
def locate_student(x):
    global like_list, board
    blank_cnt = -1
    like_cnt = -1
    pos = (0, 0)
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0: continue
            temp_like_cnt = get_like_cnt(like_list[x][1:], i, j)
            temp_blank_cnt = get_blank_cnt(i, j)
            if like_cnt < temp_like_cnt:
                pos = (i, j)
                like_cnt = temp_like_cnt
                blank_cnt = temp_blank_cnt
            elif like_cnt == temp_like_cnt and blank_cnt < temp_blank_cnt:
                blank_cnt = temp_blank_cnt
                pos = (i, j)
    # print(f"snum: {like_list[x][0]}, pos: {pos}, like_cnt: {like_cnt}, blank_cnt: {blank_cnt}")
    board[pos[0]][pos[1]] = like_list[x][0]
    return
  
# 만족도 계산
def get_ans(lis, x, y):
    cnt = 0
    ans_list = [0, 1, 10, 100, 1000]
    for d in range(4):
        nx, ny = x + dx[d] , y + dy[d]
        if OOB(nx, ny): continue
        if board[nx][ny] in lis: cnt += 1
    return ans_list[cnt]

if __name__== "__main__":
    n = int(input())
    like_list = [list(map(int, input().split())) for _ in range(n**2)]
    board = [[0 for _ in range(n)] for _ in range(n)]
    #     e   s   w  n
    dx = [0,  1,  0, -1]
    dy = [1,  0,  -1,  0]
    for i in range(n**2):
        locate_student(i)
    ans = 0
    for s in range(n**2):
        for i in range(n):
            for j in range(n):
                if board[i][j] == like_list[s][0]:
                    ans += get_ans(like_list[s][1:] ,i, j)
                    
    print(ans)


'''
**느낀점**
항상 for문에 안들어갈 수 있음에 유념하자
따라서 get_blank_cnt와 get_like_cnt의 최소값이 0 이기 때문에
for문 조건에 하나라도 만족하게끔 즉, pos를 (0, 0)이 아닌 값으로 assign하기 위해선
blank_cnt와 like_cnt를 -1로 초기화해줘야 한다.


# 도움되었던 반례
3
7 9 3 8 2 
5 7 3 8 6
3 5 2 4 9
9 6 8 3 4
8 5 3 1 6
6 3 8 5 4
2 6 4 8 7
1 8 3 4 5
4 7 9 3 8

정답 : 151
비고 :
3 5 8
9 7 6
1 2 4
=>
만약 locate_student()함수에서 blank_cnt와 like_cnt를 각각 0으로 초기화 했다면
3 5 8
9 7 6
0 2 0  인 상태에서
학생 1 이 들어갈때 pos값이 (2, 0)으로 바뀌지 않고 계속 (0, 0)에 머물기 때문에
1 5 8
9 7 6
0 2 0 이 되어버리고 최종적으로
3 5 8
9 7 6
4 2 0  가 되어버린다. 따라서 한번이라도 반복문안의 if나 elif 조건을 만족해서 pos값이 업데이트되기 위해선
blank_cnt와 like_cnt를 get_blank_cnt()와 get_like_cnt()의 최솟값인 0보다 작은 -1로 초기화를 해주어여한다!!
'''
