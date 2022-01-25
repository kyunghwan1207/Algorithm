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

''''
정보통신공학과 3학년 201700295 고경환
<주석1-본인이 작성한 알고리즘 간단하게 설명>

2차원 dp테이블을 통해서 각 원소가 될수 있는 경우의 수는 리스트의 최솟값부터 최댓값까지 이고, a, b일때 오름차순으로 만들기 위해 필요한 연산 횟수는  |a-b|입니다.
예를들어 a, b를 9, 2 일때 오름차순이 되기위해 필요한 연산 횟수는 a가 b보다 작아지기 직전 혹은 b가 a보다 커지기 직전의 값이므로 결국 a b가 서로를 향해 증-감하다가 같아질때가 최소연산횟수라고 볼 수 있습니다.
7 7, 6 6, 5 5 이러한 값들이 될때가 최소 연산 횟수입니다. 따라서 최소 |a-b|=|9-2|=7 만큼의 연산이 필요하다고 볼 수 있습니다.
따라서 큰 문제를 작은 문제로 쪼개면 "i번째 인덱스까지 오름차순이 되기 위해 필요한 최소연산횟수를 구하면 됩니다." 
A리스트에서 최솟값(min_val)과 최댓값(max_val)을 찾아서 아래의 과정으로 2차원 dp테이블을 채웁니다.
dp[i][j]는 A[i]가 j와 같을 경우 첫번째 A[i]를 오름차순으로 만들기 위해 필요한 최소연산횟수를 의미합니다.
만약 A[i]가 j와 같을때 A[i-1] <= j일 것입니다.
따라서 e가 min_val <= e <= j 이라고 하면, dp[i][j] = dp[i-1][e]의 최솟값 + |A[i]-j|가 저장됩니다.
n-1번째 인덱스까지 오름차순으로 만들기 위한 최소연산횟수가 result에 저장되어 출력합니다.

<주석2-알고리즘의 수행시간 간단하게 분석 후, 수행시간 Big-O표기>

리스트 A의 길이를 n이라고 했을때,
리스트 A의 최솟값(min_val)과 최댓값(max_val)을 찾는대 각 O(n) => 총 O(c*n)
2차원 dp테이블 초기화하고 값을 채우는데에
걸리는 시간 => O(c*n*k) 여기서 k는 리스트 A의 최대값(max_val) - 최소값(min_val)의 값입니다.(0 <= k <= 200)
n-1번째 인덱스까지 오름차순을 만들기 위한 연산횟수 중 최소를 찾기위해 O(c*k)번연산 수행합니다.
따라서 총 수행시간은 O(n*k)입니다.
'''