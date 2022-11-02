# 0730 ~ 1047
def OOB(x, y):
    return x < 0 or x >= r or y < 0 or y >= c

def shark_move():
    d_list = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3],
              [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 1, 3],
              [0, 2, 0], [0, 2, 1], [0, 2, 2], [0, 2, 3],
              [0, 3, 0], [0, 3, 1], [0, 3, 2], [0, 3, 3],
              [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 0, 3],
              [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 1, 3],
              [1, 2, 0], [1, 2, 1], [1, 2, 2], [1, 2, 3],
              [1, 3, 0], [1, 3, 1], [1, 3, 2], [1, 3, 3],
              [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 0, 3],
              [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 1, 3],
              [2, 2, 0], [2, 2, 1], [2, 2, 2], [2, 2, 3],
              [2, 3, 0], [2, 3, 1], [2, 3, 2], [2, 3, 3],
              [3, 0, 0], [3, 0, 1], [3, 0, 2], [3, 0, 3],
              [3, 1, 0], [3, 1, 1], [3, 1, 2], [3, 1, 3],
              [3, 2, 0], [3, 2, 1], [3, 2, 2], [3, 2, 3],
              [3, 3, 0], [3, 3, 1], [3, 3, 2], [3, 3, 3]]

    # **상어가 무조건 3칸은 움직여야 되기 때문에 -1 넣어야 최소 상어 위치라도 구할 수 있음**
    max_amount = -1
    for dl in range(64):
        nx, ny = shark_loc[0], shark_loc[1]
        amount = 0 # 상어가 제외시킬 물고기 수
        flag = 0 # 상어가 3번다 움직이면 1
        visited = [[False for _ in range(c)] for _ in range(r)]
        for d in d_list[dl]:
            nx, ny = nx + dsx[d], ny + dsy[d]
            if OOB(nx, ny): flag = 1;break
            # **방문한 곳 또 방문할순 있지만 amount += 시키진 x**
            if visited[nx][ny]: continue
            amount += len(fish_board[nx][ny])
            visited[nx][ny] = True

        if flag == 0 and max_amount < amount:
            max_amount = amount
            best_d = dl
            nsx, nsy = nx, ny

    dd = d_list[best_d] # 상어 best 움직임 저장
    final_shark_loc = [nsx, nsy] # 상어 최종 위치
    # 물고기 냄새
    x, y = shark_loc[0], shark_loc[1]
    for d in dd:
        x, y = x + dsx[d], y + dsy[d]
        if len(fish_board[x][y]) > 0:
            # **무조건 ++ 한번 시킬거라서 초기값을 -3줘야됨**
            smell_board[x][y] = -3
        fish_board[x][y] = [] # 물고기 제외시킴

    return final_shark_loc


def fish_move():
    global fish_board
    tboard = [[[] for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if len(fish_board[x][y]) > 0:
                for i in range(len(fish_board[x][y])):
                    fd = fish_board[x][y][i]
                    nx, ny = x + dfx[fd], y + dfy[fd]
                    cnt = 0
                    flag = 0
                    while OOB(nx, ny) or [nx, ny] == shark_loc or smell_board[nx][ny] < 0:
                        fd = (fd-1+8)%8 # **최대한 변수 활용하자! in order to 변수 업데이트**
                        nx, ny = x + dfx[fd], y + dfy[fd]
                        cnt += 1
                        if cnt >= 8: flag = 1;break
                    # **물고기 안 움직여도 리스트에 넣자!**
                    if flag == 1:
                        tboard[x][y].append(fish_board[x][y][i])
                    else:
                        tboard[nx][ny].append(fd)
    # 물고기 이동
    for x in range(r):
        for y in range(c):
            fish_board[x][y] = tboard[x][y]

if __name__ == "__main__":
    r, c = 4, 4
    m, S = map(int, input().split())
    fish_info = [list(map(int, input().split())) for _ in range(m)]
    sloc_x, sloc_y = map(int, input().split())
    shark_loc = [sloc_x-1, sloc_y-1] # 리스트로 관리 not 격자
    #      w  wn  n  en  e  es  s  ws
    dfx = [0, -1, -1, -1, 0, 1, 1, 1] # 45도 회전 -1
    dfy = [-1, -1, 0, 1, 1, 1, 0, -1]
    #      n  w  s  e
    dsx = [-1, 0, 1, 0] # 3번씩 움직
    dsy = [0, -1, 0, 1]
    fish_board = [[[] for _ in range(c)] for _ in range(r)] # []로 해서 여러물고기 가능
    smell_board = [[0 for _ in range(c)] for _ in range(r)] # -3 체크 후 ++
    # 물고기 위치 격자위에 표시
    for f in fish_info:
        fish_board[f[0]-1][f[1]-1].append(f[2]-1)

    for s in range(S):
        temp_fish_board = [[[] for _ in range(c)] for _ in range(r)]
        # 1 물고기 복제 temp
        for i in range(r):
            for j in range(c):
                temp_fish_board[i][j] = fish_board[i][j]
        # 2 물고기 이동
        fish_move() # done
        # 3 상어 이동(무조건 3칸 이동)
        shark_loc = shark_move()

        # 4 두번 전 연습에 냄새 사라짐
        for i in range(r):
            for j in range(c):
                if smell_board[i][j] < 0:
                    smell_board[i][j] += 1
        # 5 복제
        for i in range(r):
            for j in range(c):
                if len(temp_fish_board[i][j]) > 0:
                    for tfd in temp_fish_board[i][j]:
                        fish_board[i][j].append(tfd)

    # end of s
    ans = 0
    for i in range(r):
        for j in range(c):
            ans += len(fish_board[i][j])
    print(ans)
'''
느낀점
1. 문제에서 제시한 대로 잘 풀었지만 디테일한 부분 잘 잡고가자!
(상어는 무조건 3번 움직여야한다. 냄새는 한 턴 끝날때 사라진다)
2. smell_board와 fish_board 잘 분리했고, shark_loc 1차원 리스트로 관리한것 좋았다
(겹치는 경우도 스무스하게 해결가능)
3. 상어가 무조건 한번은 이동할 수 있게 amount값을 -1로 잡아주자!
(for문 안 들어갈까봐 너무 쫄지마~)
4. 좌표 초기화는 꼭 for문안에서 해주자!
(밖에서 하면 좌표 값이 계속 이어져서 변경됨ㅠ)
'''
