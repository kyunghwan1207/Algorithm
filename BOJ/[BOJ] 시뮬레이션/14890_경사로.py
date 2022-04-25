# 현재위치에 경사로를 놓을 수 있는지/없는지 -> T/F
def check_can_lay(i, j, dir):
    global M, G, l, n
    # 이미 한칸 차이나는 것은 확인했음
    if dir == 'r': # 행으로
        if M[i][j] < M[i][j+1]: # 높아지는 경사
            # M[i][j]를 포함한 왼쪽 부분에 경사로를 놓아야함.
            if j-l < -1: # 경사로 놓다가 범위를 벗어나는 경우
                return False
            for k in range(l): 
                if G[i][j-k] == 1: # 이미 경사로가 놓여져있는경우
                    return False
            for k in range(1, l):
                if M[i][j-k] != M[i][j]: # 같은 높이가 아닌경우
                    return False
            # 경사로 놓기
            for k in range(l):
                G[i][j-k] = 1
            return True
        elif M[i][j] > M[i][j+1]: # 낮아지는 경사
            # M[i][j+1]를 포함한 오른쪽 부분에 경사로를 놓아야함.
            if n-j-l < 1: # 경사로 놓다가 범위를 벗어나는 경우
                return False
            for k in range(l):
                if G[i][j+1+k] == 1: # 이미 경사로가 놓여져있는경우
                    return False
            for k in range(1, l):
                if M[i][j+1+k] != M[i][j+1]: # 같은 높이가 아닌경우
                    return False 
            for k in range(l):
                G[i][j+1+k] = 1
            return True

    if dir == 'c': # 열으로
        if M[i][j] < M[i+1][j]: # 높아지는 경사
            # M[i][j]를 포함한 위쪽 부분에 경사로를 놓아야함.
            if i-l < -1: # 경사로 놓다가 범위를 벗어나는 경우
                return False
            for k in range(l):
                if G[i-k][j] == 1: # 이미 경사로가 놓여져있는경우
                    return False
            for k in range(1, l):
                if M[i-k][j] != M[i][j]: # 같은 높이가 아닌경우
                    return False
            # 경사로 놓기
            for k in range(l):
                G[i-k][j] = 1
            return True
        elif M[i][j] > M[i+1][j]: # 낮아지는 경사
            # M[i+1][j]를 포함한 아래쪽 부분에 경사로를 놓아야함.
            if n-i-l < 1: # 경사로 놓다가 범위를 벗어나는 경우
                return False
            for k in range(l):
                if G[i+1+k][j] == 1: # 이미 경사로가 놓여져있는경우
                    return False
            for k in range(1, l):
                if M[i+1+k][j] != M[i+1][j]: # 같은 높이가 아닌경우
                    return False
            # 경사로 놓기
            for k in range(l):
                G[i+1+k][j] = 1
            return True
    return

if __name__ == "__main__":
    n, l = map(int, input().split())
    M, G = [], []
    for _ in range(n):
        M.append(list(map(int, input().split())))
    # 1~10의 숫자가 써있다.
    G = [[0 for _ in range(n)] for _ in range(n)] # 경사로 있는지/없는지 -> 1/0 기록
    cnt = 0 # 길의 개수
    # 행에서 가능한 길찾기
    for i in range(n):
        for j in range(n-1):
            # 행에서 가능한 길찾기
            if M[i][j] == M[i][j+1]: continue
            elif abs(M[i][j] - M[i][j+1]) == 1:
                if not check_can_lay(i, j, 'r'): break
            else: break

        else: # for-else 문 (for문이 정상적으로 종료되었을 경우 조건문 실행)
            cnt += 1
    G = [[0 for _ in range(n)] for _ in range(n)] # 행길 때 입력한 경사로 초기화
    for j in range(n):
        for i in range(n-1):
            # 열에서 가능한 길찾기
            if M[i][j] == M[i+1][j]: continue
            elif abs(M[i][j] - M[i+1][j]) == 1:
                if not check_can_lay(i, j, 'c'): break                
            else: break
        else:
            cnt += 1
    print(cnt)
'''
느낀점:
1. 문제에서 예시주어지면 자세히 보자 -> 문제에서 요구하는 방향 명확하게 알고가자
ex. 행길과 열길의 경사로 놓는 것은 서로 영향없었다 -> G 초기화 필요했음

2. 조건짤때 너무 암산으로 하지말고 최대한 필기구 이용해서 시각화하고 꼼꼼히 체크하자

3. 한 번에 여러개 조건을 동시에 처리할려고 하지말자 -> 한 번에 한 조건씩 해결한다는 마인드o
'''