# 앞으로 나아갈 수 있는지/없는지 -> T/F
def check_can_go(r, c, n):
    if r >= n or c >= n or r < 0 or c < 0:
        return False
    return True
# 나아가는 좌표가 몸이랑 만나는지/아닌지 -> T/F
def check_meet_body(r, c, tail_idx):
    global snake
    for i in range(tail_idx, len(snake)):
        if snake[i][0] == r and snake[i][1] == c:
            return True
    return False

'''start of main'''
n = int(input())
M = [[0 for _ in range(n)] for _ in range(n)]
k = int(input())
for _ in range(k):
    apple_r, apple_c = map(int, input().split())
    apple_r -= 1; apple_c -= 1
    M[apple_r][apple_c] = 1
l = int(input())
command = []
for _ in range(l):
    x, cmd = input().split()
    command.append([int(x), cmd])
    # 동 남  서 북 (index ++ -> 오른쪽회전, index-- -> 왼쪽회전)
dr = [0, 1,  0,-1]
dc = [1, 0, -1, 0]
t = 0 # 시간
r, c = 0, 0 # 뱀의 시작점
snake = [[r, c]] # 초기 길이 1
tail_idx = 0 # Queue처럼 동작하기위해 포인터를 하나씩 오른쪽으로 움직이기 위해 사용
idx_command = 0 # command의 순서에 따라서 몇초에 방향전환할지check
idx_direction = 0 # dr, dc를 적절히 회전시키기 위해서 필요
while True:
    t += 1
    # 현재 방향으로 전진
    r += dr[idx_direction]
    c += dc[idx_direction]
    if not check_can_go(r, c, n): break # 맵 벗어나면 게임종료
    if check_meet_body(r, c, tail_idx): break # 몸이랑 만나면 게임종료
    snake.append([r, c]) # 머리를 다음칸에 위치
    # 사과 만났을때 대응
    if M[r][c] == 1:
        M[r][c] = 0 # 사과가 없어진다
    # 사과 안 만났을 떄
    else:
        tail_idx += 1 # popleft() 한것과 동일함
    # 나아갈 방향설정하기
    if idx_command < len(command) and t == command[idx_command][0]: # command를 수행할 시간인지 check
        if command[idx_command][1] == 'D': # Right -> idx_dirc++
            idx_direction += 1
            if idx_direction > 3:
                idx_direction = 0
        elif command[idx_command][1] == 'L': # Left -> idx_dirc--
            idx_direction -= 1
            if idx_direction < 0:
                idx_direction = 3
        idx_command += 1
print(t)
'''end of main'''