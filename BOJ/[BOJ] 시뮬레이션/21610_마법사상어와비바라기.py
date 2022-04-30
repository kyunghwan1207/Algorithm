# 1946 -> 2110

# 구름이 생겼었던 곳을 기록해야하니까 bool타입으로배열만들어서 구름이 생성될때 생성되도되는지 check하자
import sys
input = sys.stdin.readline

def OOB(r, c):
    global N
    return r < 0 or r >= N or c < 0 or c >= N

# 구름이 위치할 좌표를 리스트에 담아서 return
def make_cloud(c):
    global A, N, cloud_existed
    cloud_loc = []
    for i in range(N):
        for j in range(N):
            if cloud_existed[i][j] != c and A[i][j] >= 2:
                cloud_loc.append([i, j])
                A[i][j] -= 2
    return cloud_loc

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    cmd = [] # [d_i, s_i]
    for _ in range(M): 
        d, s = map(int, input().split())
        cmd.append([d-1, s])
    # d_i: 0-w, 1-nw 2-n, 3-ne, 4-e, 5-es, 6-s, 7-ws
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    dc = [-1, -1, 0, 1, 1, 1, 0, -1] 

    # 비바라기 시작
    cloud_existed = [[-1 for _ in range(N)] for _ in range(N)] # cmd가 적용된 인덱스를 기록함으로써 구름이 있었던 곳 표시
    cloud_location = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]] # cloud location
    for c in range(len(cmd)):
        # cloud_existed = [[False for _ in range(N)] for _ in range(N)] # 구름이 존재했었는지 기록
        for i in range(len(cloud_location)): # Step1. 모든 구름이 d_i방향으로 ~
            s = cmd[c][1]
            d = cmd[c][0]
            cloud_r = cloud_location[i][0]
            cloud_c = cloud_location[i][1]
            nr = (cloud_r + dr[d]*s)%N
            nc = (cloud_c + dc[d]*s)%N
            A[nr][nc] += 1 # Step2. 물의 양 ++
            cloud_location[i] = [nr, nc]
            cloud_existed[nr][nc] = c # 구름 사라진곳 채크
        # 4. water copy
        for p in cloud_location:
            for i in range(1, 8, 2): # 대각선탐색위함
                # 1, 3, 5, 7
                p_r = p[0] + dr[i]
                p_c = p[1] + dc[i]
                if not OOB(p_r, p_c):
                    if A[p_r][p_c] != 0:
                        A[p[0]][p[1]] += 1 # 4. 대각선방향 ~ 바구니 물양 증가
        # cloud_location = [] # 3. 구름이 모두 사라진다.
        cloud_location = make_cloud(c) # 3, 5. 바구니 물 양이 2이상인 칸 ~

    ans = 0
    for i in range(N):
        for j in range(N):
            ans += A[i][j] 
    print(ans)


'''
1차시도 - 실패
Pypy3는 통과하지만 Python3는 시간초과
<개선방안>
1. cloud_existed 를 매번 False로 초기화하지말고 range(len(cmd))로 해서 cmd마다 인덱싱을 둬서 
매번 초기화하지않고 인덱스 확인방법으로 해결하자
2. while s > 0 : s -= 1 이부분을 한번에 steop진행할 수 있도록
계산방법을 강구해서 s번 반복대신 한번에 바로 갈 수 있는 공식?을 유도해보자
=> 끝과끝이 연결되어있다 -> 원형큐 처럼 생각하자 -> % N 연산 수행
'''


