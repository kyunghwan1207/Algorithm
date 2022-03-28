import sys

input = sys.stdin.readline

# A2을 입력으로 주면 (6, 0)을 return
def location(point):
    # 숫자는 8을 빼면 되고, 알파벳은 ord한거에 65를 빼면 된다
    c, r = point[0], point[1]
    return 8-int(r), ord(c)-65

# (r, c)좌표가 체스판을 벗어났는지(T)/안 벗어났는지(F) 확인해주는 함수
def out(r, c):
    if r < 0 or c < 0 or r > 7 or c > 7:
        return True
    else:
        return False

'''start of main'''    
# 열: ord('A') = 65 ~ print('H') = 72 -> ord chr
# 행: 1 ~ 8
move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dr =   [0,   0,   1,   -1,  -1,   -1,    1,    1]
dc =   [1,  -1,   0,    0,   1,   -1,    1,   -1]
k, s, n = input().split()
r_king, c_king = location(k)
r_stone, c_stone = location(s)
for _ in range(int(n)):
    d = move.index(input().split('\n')[0]) # 명령어 입력
    nr, nc = r_king + dr[d], c_king + dc[d] # 킹이 이동할 좌표
    if not out(nr, nc):
        if r_stone == nr and c_stone == nc:
            if not out(r_stone + dr[d], c_stone + dc[d]):
                r_king = nr
                c_king = nc
                r_stone += dr[d]
                c_stone += dc[d]
        else:
            r_king = nr
            c_king = nc
            
r_king_final = abs(r_king - 8)
c_king_final = chr(c_king + 65)
print(c_king_final + str(r_king_final))
r_stone_final = abs(r_stone - 8)
c_stone_final = chr(c_stone + 65)
print(c_stone_final + str(r_stone_final))
'''end of main'''

'''
<알고리즘 설명>
문제의 그림대로 행, 열을 기준으로 좌측상단을 (0, 0), 우측하단을 (7, 7)로 보고 풀이진행 하였음.
Step1. 명령어에 따라 적절히 이동할 수 있도록 리스트로 매핑이후 사용할 변수 할당
Step2. 명령어를 입력받고 킹이 이동할 좌표를 설정함 -> (nr, nc) 할당
Step3. out함수를 통해 (nr, nc), 돌이 이동할 좌표(r_stone + dr[d], c_stone + dc[d])가 유효한지 확인 후 적절한 로직수행

<수행시간 분석>
움직이는 횟수를 n, 상수를 c라고 하면
Step1.   O(c)
Step2,3. O(n*c) (이유: n만큼 반복해야 하므로)
=> 총 수행시간: O(c) + O(n*c) = O(n)
'''
