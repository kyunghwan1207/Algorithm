import sys
input = sys.stdin.readline


def update_count_blank(current_idx, copy_board, count_blank):
    global N, M, board, cctv, res
    if current_idx == len(cctv):
        return count_blank # 빈칸 갯수
    r, c, type = cctv[current_idx]
    dir_list = cctv_dic[type] # ex. [[0, 1], [1, 2], [2, 3], [3, 0]]
    copy_copy_board = [[0 for _ in range(M)] for _ in range(N)]
    for dir in dir_list:
        copy_count_blank = count_blank
        for i in range(N):
            for j in range(M):
                copy_copy_board[i][j] = copy_board[i][j]
        for d in dir:
            # 0-east
            if d == 0:
                for i in range(c+1, M):
                    if copy_copy_board[r][i] == 0: 
                        copy_count_blank -= 1
                        copy_copy_board[r][i] = 7 # 이미봣음을 체크
                    elif copy_copy_board[r][i] == 6: break # 벽 만나면 break
            # 1-north
            elif d == 1:
                for i in range(r-1, -1, -1):
                    if copy_copy_board[i][c] == 0: 
                        copy_count_blank -= 1
                        copy_copy_board[i][c] = 7
                    elif copy_copy_board[i][c] == 6: break
            # 2-west
            elif d == 2:
                for i in range(c-1, -1, -1):
                    if copy_copy_board[r][i] == 0: 
                        copy_count_blank -= 1
                        copy_copy_board[r][i] = 7
                    elif copy_copy_board[r][i] == 6: break
            # 3-south
            elif d == 3:
                for i in range(r+1, N):
                    if copy_copy_board[i][c] == 0: 
                        copy_count_blank -= 1
                        copy_copy_board[i][c] = 7
                    elif copy_copy_board[i][c] == 6: break
        res = min(res, update_count_blank(current_idx+1, copy_copy_board, copy_count_blank))
    return res


if __name__ == "__main__":
    N, M = map(int, input().split())
    # 0-east, 1-north, 2-west, 3-south (= index-direction)
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    board = []
    cctv = [] # [cctv행위치, cctv열위치, cctv_type]
    res = 2147000000
    cctv_dic = {
        1: [[0], [1], [2], [3]],
        2: [[0, 2], [1, 3]],
        3: [[0, 1], [1, 2], [2, 3], [3, 0]],
        4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        5: [[0, 1, 2, 3]]
    }
    for _ in range(N):
        board.append(list(map(int, input().split())))
    count_blank = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                count_blank += 1
            elif 0 < board[i][j] < 6:
                cctv.append([i, j, board[i][j]]) # cctv정보입력
    print(update_count_blank(0, board, count_blank))

'''
<느낀점>
1. 재귀함수 쓸 때는 전역변수 사용x 무조건 local variable로 사용하자
그래야 다음에 재귀호출한 부분에서 우리가 의도했던대로 변수값이 바뀜.
2. 리스트 copy할때 2차원 이상이라면 단순히 = 으로 assign하지 말고 for문으로 원소하나씩 값 assign하자
'''