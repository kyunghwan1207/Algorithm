import math
from itertools import permutations

def is_prime(x, ans_list):
    if x in ans_list or x <= 1:
        return False
    else:
        ans_list.append(x)
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    ans_list = []
    n = len(numbers)
    for i in range(1, n+1):
        lis = list(permutations(numbers, i))
        for item in lis:
            num = ''
            for j in range(i):
                num += item[j]
            # print(int(num))
            if is_prime(int(num), ans_list):
                answer += 1
    return answer
