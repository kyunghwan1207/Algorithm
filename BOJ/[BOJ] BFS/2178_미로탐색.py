import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        input_ = input()
        temp = input_[:-1] # '\n'을 제외시키기 위함
        board.append(list(map(int, temp))) # temp: '1011111'
    #     e   n   w    s
    dx = [0,  1,  0,  -1]
    dy = [1,  0,  -1,  0]
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if board[nx][ny] == 0: continue
            if board[nx][ny] == 1:
                q.append((nx, ny))
                board[nx][ny] = board[x][y] + 1
    print(board[n-1][m-1])
'''
느낀점
1. 최단경로 구하기이므로 BFS사용하자
2. board[][] 값을 계속 업데이트 할 것이므로 별도의 visited[][] 리스트 없이 board[][]==1로만 조건 두어도
 처음 방문하는 노드 탐색할 수 있음
'''