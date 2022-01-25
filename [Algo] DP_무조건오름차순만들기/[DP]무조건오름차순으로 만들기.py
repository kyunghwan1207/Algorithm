import math
def solve(A):
    for i in range(1, n):# dp[0][~]은 solve함수 호출전에 미리 채워놓았음.
        min_val_temp = math.inf # 정수로 나타낼 수 있는 최댓값 저장 약 2147000000
        for j in range(min_val, max_val+1): #각 원소가 가질 수 있는 값의 범위는 리스트A의 최소값~최대값이다.
            min_val_temp = min(min_val_temp, dp[i-1][j])
            # dp[i][j]는 A[i]가 j와 같을 경우 첫번째 A[i]를 오름차순으로 만들기 위해 필요한 최소연산횟수를 의미함.
            # A[i]가 j와 같을때 A[i-1] <= j일 것이다.
            # 따라서 e가 min_val <= e <= j 이라고 하면, dp[i][j] = dp[i-1][e]의 최솟값 + |A[i]-j|
            if A[i] > j:
                dp[i][j] = min_val_temp + (A[i]-j)
            else:
                dp[i][j] = min_val_temp + (j-A[i])
    result = math.inf
    for k in range(min_val, max_val+1):
        result = min(result, dp[n-1][k]) #n-1번째 인덱스까지 오름차순으로 만들기 위한 최소연산횟수가 result에 저장됨
    return result

'''start of main'''
A = []
min_val = math.inf
max_val = 0

A = [int(x) for x in input().split()]
n = len(A)
min_val = min(A)
max_val = max(A)
dp = [[0]*(max_val+1) for _ in range(n)] #min_val나 max_val을 인덱스값과 동일하게 접근하기 위함(0은 사용x)
for i in range(min_val, max_val+1):
    if A[0] > i:
        dp[0][i] = A[0] - i
    else:
        dp[0][i] = i - A[0]
print(solve(A))
'''end of main'''