# 16시 20분 시작 -> 18시까지 보자
import itertools

def get_distance(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2) # 1씩 증가했을 지라도 그냥 뺄샘하면 0,0 일때랑 동일하다
# (r, c) -> (1, 1)부터 시작
# 집과 치킨집의 '최소' 거리 == 해당 집의 치킨 거리 값
if __name__ == "__main__":
    n, m = map(int, input().split()) # m개의 치킨집만을 남겨야한다
    board = []
    house = []
    chicken = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    # 0: 빈칸, 1: 집, 2: 치킨집
    chicken_idx = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: # 집일때
                house.append([i, j])
            elif board[i][j] == 2: # 치킨집일때
                chicken.append([i, j])
                chicken_idx += 1
    chicken_distance = [[] for _ in range(len(house))] # idx: 집순서, val: [각 치킨집들의 치킨거리값] -> len(house) x len(chicken) 의 크기를 가질 것임
    comb_list = []
    for i in range(chicken_idx):
        comb_list.append(i) # 치킨집을 0부터 idx적용했음.
    comb_list = list(itertools.combinations(comb_list, m)) # [(0, 1, 2), (~) ~]
    # 집기준으로 각 집들이 얼마만큼의 치킨거리를 가졌는지 체크
    for i in range(len(house)):
        for j in range(len(chicken)):
            chicken_distance[i].append(get_distance(house[i][0], house[i][1], chicken[j][0], chicken[j][1]))

    ans_list = [0] * len(comb_list)
    for i in range(len(comb_list)):
        for p in range(len(chicken_distance)):
            min_val = 2147000000
            for j in comb_list[i]:
                min_val = min(min_val, chicken_distance[p][j])
            ans_list[i] += min_val

    print(min(ans_list))

# 1차시도 - 실패
'''
m개를 선출하는 기준이 현재는 그냥 전체집을 기준으로 치킨거리값을 합했을 때 최소값을 기준으로
앞에서 부터 m개를 선출했는대 다른 조건이 필요해보인다.
-> m개를 고르는 것은 맞다
하지만 꼭 m개를 다 골라야하는가? -> 문제에서 최대m개라고 했으니까
우리는 1 ~ M개 까지의 모든 경우를 고려해보고
그 중 최소값을 출력하자!
'''
# 2차시도 - 실패
'''
M개를 거를때 총합을 통해서 거리값이 제일 작은 경우기준으로 오름차순해서
하지말고 -> 그냥 조합(itertools.combinations)써서 해결하자
'''
# 3차시도 - 성공
'''
느낀점
1. 조건을 너무 복잡하게 생각하지말고 만약, 예외적인 경우를 찾기 힘들다면
조합으로 모든 경우의 수를 다 해보는 것도 좋다!
2. 직관적으로 치킨집 M개를 모두 보유하는게 최소치킨거리를 제공할 것이다!
'''