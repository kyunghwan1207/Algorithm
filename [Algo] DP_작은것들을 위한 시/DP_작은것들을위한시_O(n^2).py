A = [int(x) for x in input().split()]
n = len(A)
dp = [0]*n
for i in range(n):
    current_min = A[i]
    sum_val = 0
    for j in range(i, n):
        if current_min >= A[j]:
            current_min = A[j]
        sum_val += current_min
    dp[i] = sum_val
answer = 0
for k in range(len(dp)):
    answer += dp[k]
print(answer)

'''
<알고리즘 설명>
Step1. 리스트 A에 원소 입력
Step2. 탐색의 시작점을 잡기위해 i변수 및 사용할 변수 초기화
Step3. i부터 n-1까지 최솟값을 유지하면서 sum_val에 더해가며 for문이 끝나면 dp[i]에 sum_val을 저정함
Step4. 최종정답 출력을 위해 dp를 순회하면서 answer변수에 더함

<수행시간 분석>
입력되는 원소의 개수를 n개라고 하면
Step1. O(n)
Step2, 3 -> O(n^2)  (이유: 이중반복문)
Step4. O(n)
=> 총 수행시간: O(n) + O(n^2) + O(n) = O(n^2)
'''