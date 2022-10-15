# 구슬 파괴하기
def breakBiz(d, s):
    res = []
    step = s
    nx, ny = start, start
    while step:
        step -= 1
        nx, ny = nx + dx[d], ny + dy[d]
        # 어차피 s <= (n-1)/2 이기 때문에 범위벗어나는거 체크필요x
        res.append([nx, ny])
    return res

# 구슬 움직이기
def moveBiz(biz1d):
    biz1d_temp = [0] * (n ** 2 - 1)
    bidx = 0
    for i in range(len(biz1d)):
        if biz1d[i] == 0: continue
        cnt = biz1d[i]
        biz1d_temp[bidx] = cnt
        bidx += 1
    for i in range(len(biz1d)):
        biz1d[i] = biz1d_temp[i]
    return biz1d

# 구슬 변화하기
def changeBiz(biz1d):
    temp_biz1d = [0]*(n**2 - 1)
    curr_num = biz1d[0]
    cnt = 1
    bidx = 0
    for i in range(1, len(biz1d)):
        if curr_num == biz1d[i]:
            cnt += 1
        elif curr_num != biz1d[i]:
            if bidx >= len(biz1d): break
            temp_biz1d[bidx] = cnt
            if bidx+1 >= len(biz1d): break
            temp_biz1d[bidx+1] = curr_num
            bidx += 2
            # if bidx >= len(biz1d): break
            curr_num = biz1d[i]
            cnt = 1
            if biz1d[i] == 0: break

    for i in range(len(biz1d)):
        biz1d[i] = temp_biz1d[i]
    return biz1d

# 2D 좌표정보를 1D로 매핑
def map2Dto1D(board2d, board1d):
    cnt = 0 # 방향 바꾼 횟수겸 다음으로 전진할 방향
    step = 0 # 전진할 횟수
    nx, ny = start, start
    flag= True
    bidx = 0 # 1D에 정보 채울 위치
    while flag:
        if cnt%2 == 0:
            step += 1
        for _ in range(step):
            nx, ny = nx + d1x[cnt], ny + d1y[cnt]
            board1d[bidx] = [nx, ny] # 2D 좌표정보를 1D에서 관리
            biz1d[bidx] = board2d[nx][ny] # 구슬 정보는 다른 리스트에서 관리(moveBiz()할 때 편하기 위함)
            bidx += 1
            if nx == 0 and ny == 0: flag = False;break
        cnt = (cnt+1)%4
    return board1d

if __name__ == "__main__":
    n, m = map(int, input().split())
    start = n//2 # 시작좌표
    board2d  = []
    #     n  s  w  e
    dx = [-1, 1, 0, 0]
    dy = [0,  0,-1, 1]
    # 2D->1D 할 때 사용할 것
    # w  s  e  n
    d1x = [0, 1, 0, -1]
    d1y = [-1, 0, 1, 0]
    ans_list = [0]*4
    for _ in range(n):
        board2d.append(list(map(int, input().split())))
    # 가운데 상어의 좌표는 필요 없기 때문에 n**2에서 -1을 해준다
    board1d = [0] * (n ** 2 - 1)
    biz1d = [0] * (n ** 2 - 1)

    # 2차원 좌표 정보를 1차원으로 관리
    board1d = map2Dto1D(board2d, board1d)

    for _ in range(m):
        d, s = map(int, input().split())
        d -= 1
        break_list = breakBiz(d, s)
        break_cnt = len(break_list)

        # 뱅글뱅글 도는것과 마찬가지기 때문에 break_list[]값은 board1d[]를
        # 순차적으로 돌면서 한번만 체크하면서 0으로 만들어줘도된다.

        # 구슬 파괴된 것을 1d에 반영
        bidx = 0
        for i in range(len(board1d)):
            if board1d[i] == 0: break
            x, y = board1d[i]
            if bidx >= break_cnt: break
            if break_list[bidx][0] == x and break_list[bidx][1] == y:
                biz1d[i] = 0
                bidx += 1
        # 구슬 움직이기
        biz1d = moveBiz(biz1d)
        # 구슬 폭발시키기
        flag= True # 구슬 폭발을 계속해야할지 여부
        while flag:
            flag = False
            curr_num = biz1d[0]
            cnt = 1
            for i in range(1, len(biz1d)):
                if curr_num == biz1d[i]:
                    cnt += 1
                elif curr_num != biz1d[i]:
                    if cnt>=4:
                        flag = True
                        ans_list[curr_num] += cnt
                        for c in range(1, cnt+1):
                            biz1d[i-c] = 0
                    if biz1d[i] == 0: break # **0 만나면 break!**
                    curr_num = biz1d[i]
                    cnt = 1
            # 구슬 움직이기
            biz1d = moveBiz(biz1d)
        # 폭발완료 후 구슬 변화시키기
        biz1d = changeBiz(biz1d)

    ans = 0
    for i in range(1, 4):
        ans += i*ans_list[i]
    print(ans)

'''
느낀점
1. [문제잘읽자!] 문제를 잘 읽자 (폭발한 구슬의 갯수이니까 폭발한거만 cnt_list에 넣기)
2. [리스트이동문제] move_biz(); 동일 리스트안에서 이동이 발생할 경우 별도의 리스트둬서 copy하자
3. [초기값문제] 폭발하기에서 num을 board1d[0]으로이미 초기화했으니까 [1 ~ len(board1d)-1]까지 탐색하면됨 
4. [코드작성 순서문제] sidx = i; num = board1d[sidx]하기전에 cnt_list[num] += cnt 하자!
5. 예외적인 TC 잘 만들어서 오류 잘 잡았다
6. 구슬폭발 시킬 떄, curr_num != biz1d[i] 일 때,
bizid[i]가 0일 수도 있는 경우 고려하자!
3 1
1 1 1
1 0 1
1 1 1
2 1
> 7
'''
