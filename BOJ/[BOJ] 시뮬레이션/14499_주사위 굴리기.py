# 갈수 있는지/없는지 -> T/F
def check_can_go(x, y, n, m):
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    return True


def roll_dice(dir):
    global horizen_eye
    global vertical_eye
    if dir == 1: # east
        v_last_temp = vertical_eye[-1]
        h_last_temp = horizen_eye[-1]

        horizen_eye[-1] = horizen_eye[1]
        horizen_eye[1] = horizen_eye[0]
        horizen_eye[0] = v_last_temp
        vertical_eye[-1] = h_last_temp

        vertical_eye[1] = horizen_eye[1]

    elif dir == 2: # west
        h_first_temp = horizen_eye[0]
        v_last_temp = vertical_eye[-1]

        horizen_eye[0] = horizen_eye[1]
        horizen_eye[1] = horizen_eye[2]
        horizen_eye[2] = v_last_temp
        vertical_eye[-1] = h_first_temp

        vertical_eye[1] = horizen_eye[1]

    elif dir == 3: # north
        v_first_temp = vertical_eye[0]
        for i in range(3):
            vertical_eye[i] = vertical_eye[i+1]
        vertical_eye[-1] = v_first_temp

        horizen_eye[1] = vertical_eye[1]
        
    elif dir == 4: # south
        v_last_temp = vertical_eye[-1]
        for i in range(3, 0, -1):
            vertical_eye[i] = vertical_eye[i-1]
        vertical_eye[0] = v_last_temp

        horizen_eye[1] = vertical_eye[1]
        
    return


if __name__ == "__main__":
    n, m, x, y, k = map(int, input().split())
    M = []
    for _ in range(n):
        M.append(list(map(int, input().split())))
    # 0 ~ 9가 지도위에 써있음.
    command = list(map(int, input().split()))
    #     - 동-1, 서-2, 북-3, 남-4
    dx = [0, 0,   0,   -1,    1] # 행 -> 인덱스 그대로 사용하기 위해 인덱스 1부터 시작
    dy = [0, 1,   -1,   0,    0] # 열
    horizen_eye = [0, 0, 0] # 문제예시의 경우: [4, 1, 3]
    vertical_eye = [0, 0, 0, 0] # 문제예시의 경우: [2, 1, 5, 6] 
    # vertical_eye[1]: top, vertical_eye[3]: bottom
    for i in range(len(command)):
        x += dx[command[i]]
        y += dy[command[i]]
        if not check_can_go(x, y, n, m):
            x -= dx[command[i]]
            y -= dy[command[i]]
            continue
        roll_dice(command[i]) # 주사위 굴리기
        if M[x][y] == 0:
            M[x][y] = vertical_eye[3]
        else:
            vertical_eye[3] = M[x][y]
            M[x][y] = 0
        print(vertical_eye[1]) # 위를 바라보는 값 출력