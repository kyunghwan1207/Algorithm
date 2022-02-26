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

'''
<알고리즘 설명>
원반 n개를 현재막대(1번막대)에서 목적지막대(3번막대)로 옮기기 위해선
Step1.[12번째 줄]: n-1개를 1번막대에서 3번막대를 거쳐서 보조막대(2번막대)에 둡니다. 
Step2.[13번째 줄, 14번째 줄]: 나머지 제일 큰 원반 1개를 3번막대로 옮기면됩니다.
Step3.[15번째 줄]: 2번막대에 있는 n-1개의 원반을 1번막대를 거쳐서 3번막대로 옮깁니다.

<수행시간 분석-귀납적 정의>
원반의 개수를 n이라고 하고, n개의 원반을 옮기는 이동횟수를 a_n이라고 하면 (원반 1개를 옮기는 횟수는 1이므로 a_1 = 1)
Step1~Step3까지의 수행시간을 보았을때 점화식으로 표현하면 a_n = a_n-1 + 1 + a_n-1 이므로
a_n = 2*a_n-1 + 1 입니다. 따라서 양변에 1을 더해주면
a_n + 1 = 2(a_n-1 + 1) 이 되므로 b_n = a_n + 1이라고 한다면
위의 식은 다음과 같이 나타낼 수 있습니다.
b_n = 2*b_n-1 이떄 b_1 = a_1 + 1 = 2가 되므로
b_n은 초항: 2, 공비: 2인 등비수열임을 알 수 있습니다.
그러므로 b_n을 n에 관한식으로 나타내면 b_n = 2(2^(n-1) - 1) / (2 - 1) = 2^n - 2가 됩니다.
따라서 a_n = b_n - 1 = 2^n - 1이 됩니다. 위 알고리즘에서 cnt가 a_n을 의미합니다. 마지막에 cnt만큼 for문을 수행합니다.
=> 총 수행시간: O(2^n)
'''
