def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def canGo(x, y):
    if OOB(x, y): return False
    if x == shark_x and y == shark_y: return False
    if smell_board[x][y] < 0: return False
    return True


def moveFish(board):
    temp_board = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] == []: continue
            dir_list = board[x][y]
            for i in range(len(dir_list)):
                dir = dir_list[i]
                nx, ny = x + dx[dir], y + dy[dir]
                flag = True
                nd = dir
                if not canGo(nx, ny):
                    nd = dir-1
                    flag = False
                    for _ in range(8):
                        nx, ny = x + dx[nd], y + dy[nd]
                        if canGo(nx, ny): flag = True;break
                        nd = (nd - 1 + 8) % 8
                # 물고기가 한칸 전진할 수 있다면(새로운위치로 세로운 방향)
                if flag == True:
                    temp_board[nx][ny].append(nd)
                # 물고기가 한칸 전진할 수 없다면(원래 대로 둔다)
                elif flag == False:
                    temp_board[x][y].append(dir)
    # 원래 board[][]로 반영
    for x in range(n):
        for y in range(n):
            board[x][y] = temp_board[x][y]
    return board

def moveShark(x, y, move_cnt, fish_cnt, move_step, visited):
    global max_fish_cnt, shark_x, shark_y, move_history
    dsx = [-1, 0, 1, 0]
    dsy = [0, -1, 0, 1]
    if move_cnt == 3:
        if max_fish_cnt < fish_cnt:
            max_fish_cnt = fish_cnt
            shark_x, shark_y = x, y
            for i in range(len(move_step)):
                move_history[i] = move_step[i]
        return
    for d in range(4):
        nx, ny = x + dsx[d], y + dsy[d]
        if OOB(nx, ny): continue
        if not visited[nx][ny]:
            visited[nx][ny] = True
            fcnt = len(board[nx][ny])
            move_step.append([nx, ny])
            moveShark(nx, ny, move_cnt+1, fish_cnt+fcnt, move_step, visited)
            visited[nx][ny] = False
            move_step.pop()
        else:
            move_step.append([nx, ny])
            moveShark(nx, ny, move_cnt+1, fish_cnt, move_step ,visited)
            move_step.pop()


if __name__ == "__main__":
    m, S = map(int, input().split())
    n = 4
    #    w   wn  n  ne   e   es  s  sw
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    fish_info = []
    board = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        fx, fy, d = map(int, input().split())
        fish_info.append([fx-1, fy-1, d-1])
        board[fx-1][fy-1].append(d-1)
    x, y = map(int, input().split())
    shark_x, shark_y = x-1, y-1
    smell_board = [[0]*n for _ in range(n)]
    for s in range(S):
        temp = [[[] for _ in range(n)]for _ in range(n)]
        for x in range(n):
            for y in range(n):
                temp[x][y] = board[x][y]
        board = moveFish(board)
        max_fish_cnt = -1
        visited = [[False]*n for _ in range(n)]
        move_history = [0, 0, 0]
        # update (shark_x, shark_y), move_history[]
        moveShark(shark_x, shark_y, 0, 0, [], visited)
        for x in range(n):
            for y in range(n):
                if [x, y] in move_history:
                    if len(board[x][y]) > 0:
                        board[x][y] = []
                        smell_board[x][y] = -3

        # 냄새 사라짐
        for x in range(n):
            for y in range(n):
                if smell_board[x][y] < 0:
                    smell_board[x][y] += 1
        # 복제 마법 발동
        for x in range(n):
            for y in range(n):
                if temp[x][y] == []: continue
                for tem in temp[x][y]:
                    board[x][y].append(tem)

    # 남아있는 물고기 수 구하기
    ans = 0
    for x in range(n):
        for y in range(n):
            ans += len(board[x][y])
    print(ans)
'''
느낀점
1. 문제에서 제시한 대로 잘 풀었지만 디테일한 부분 잘 잡고가자!
(상어는 무조건 3번 움직여야한다. 냄새는 한 턴 끝날때 사라진다)
2. smell_board와 fish_board 잘 분리했고, move_history 1차원 리스트로 관리한것 좋았다
3. 좌표 초기화는 꼭 for문안에서 해주자!
(밖에서 하면 좌표 값이 계속 이어져서 변경됨ㅠ)
'''
