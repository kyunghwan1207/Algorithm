import sys
input = sys.stdin.readline
n = int(input())
cnt = 0 # 총 수행횟수 저장
answer = [] # 수행 과정 저장 ex. [ [1, 2], [2, 3], ... ] 형태
def solution(n, first, temp, last):
    global cnt
    if n == 1: # base case(바닥조건)
        cnt += 1
        answer.append([first, last])
        return
    solution(n-1, first, last, temp)
    cnt += 1
    answer.append([first, last]) # first에서 temp로 옮길 것이기 때문에 변수명은 헷갈리지만 파라미터 순서상 (현재, 보조, 목적지)이므로
    solution(n-1, temp, first, last)

'''start of main'''
#solution(n, first, temp, last) # (원판갯수, 현재막대, 거쳐갈 보조막대, 목적지 막대)
solution(n, 1, 2, 3)
print(cnt)
for i in range(cnt):
    print(answer[i][0], answer[i][1])
'''end of main'''