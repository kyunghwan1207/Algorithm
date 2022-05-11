if __name__ == "__main__":
    N = int(input())
    #     동, 북, 서, 남,
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    curve = []
    for _ in range(N):
        x, y, d, g = map(int, input().split())
        # x, y 반대로 생각하자
        x, y = y, x
        dragon = [[], [], [d]] # 이전세대(idx: -1), 현재세대(idx: 1) 왓다갓다 하기 위함
        p = 1 #  now_gen 가르킴
        # '0 1 2 1 2 3 2 1' 2 3 0 3 2 3 2 1
        for i in range(g):
            dragon[p] = dragon[-p] + [0]*len(dragon[-p])
            for j in range(len(dragon[-p]), len(dragon[p])):
                dragon[p][j] = (dragon[-p][len(dragon[-p])-j-1] + 1) % 4
            p *= -1

        nx, ny = x, y
        curve.append([nx, ny])
        for i in dragon[-p]:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx <= 100 and 0 <= ny <= 100:
                curve.append([nx, ny])

    cnt = 0
    board = [[0 for _ in range(101)] for _ in range(101)] # 0 <= x, y <= 100 이기때문
    for c in curve:
        board[c[0]][c[1]] = 1
    for i in range(100): # i+1 도 볼 것 이므로 99까지 범위설정해도 ok
        for j in range(100):
            if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
                cnt += 1
    print(cnt)
'''
<느낀점>
1. 규칙을 찾을 수 있도록 노력하자
2. 문제가 이해 안 되어도 일단 문제에서 제시한 요건에 맞게 손으로 써 보면서 규칙을 찾아보자
3. 왓다갓다 할때는 3차원 리스트로 1, -1 인덱스 번갈아가면서 사용하자
4. 비효율적인 코드는 최대한 효율적으로 바꿔서 제출하자
'''







