
def belt_rotate():
    global belt
    nn = len(belt) # nn == 2n
    nn_temp = belt[nn-1]
    for i in range(nn-2, -1, -1):
        belt[i+1] = belt[i]
    belt[0] = nn_temp
    return
# n이 되면 즉시 내림
def robot_rotate():
    global robot, n, cnt
    for i in range(n-2, -1, -1):
        robot[i+1] = robot[i]
    robot[0] = 0
    robot[n-1] = 0 # '내리는 위치'에 로봇이 있으면 즉시 내린다.
    return

if __name__ == "__main__":
    n, k = map(int, input().split())
    belt = list(map(int, input().split()))
    robot = [0]*n
    cnt = 0 # 내구도가 0인 칸의 갯수
    level = 0
    while True:
        level += 1
        belt_rotate(); robot_rotate()
        for i in range(n-2, -1, -1):
            if robot[i] != 0 and robot[i+1] == 0 and belt[i+1] >= 1:
                robot[i+1] = robot[i]
                robot[i] = 0
                belt[i+1] -= 1
                if belt[i+1] == 0: cnt += 1
            robot[n-1] = 0 # n 즉, '내리는 위치'에 로봇이 있으면 즉시 내린다.
        if belt[0] != 0:
            robot[0] = 1
            belt[0] -= 1
            if belt[0] == 0: cnt += 1
        if cnt >= k: print(level); break
