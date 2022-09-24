from itertools import permutations
        
def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    lis = [i for i in range(1, n+1)]
    case_lis = list(permutations(lis, n))
    # print(case_lis)
    for case in case_lis:
        temp_k = k
        cnt = 0
        for c in case:
            if dungeons[c-1][0] <= temp_k:
                temp_k -= dungeons[c-1][1]
                cnt += 1
        answer = max(answer, cnt)
    return answer
