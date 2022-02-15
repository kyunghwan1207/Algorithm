import sys, math
def mse(left, right):
	sum_squared_val = dp2[right] - dp2[left-1]
	sum_val = dp1[right] - dp1[left-1]
	return sum_squared_val - (sum_val*sum_val)/(right-left+1)
def solve(B, n):
	for i in range(2, B+1): # 그룹이 i(=2, ... B)개 일때 만들어지는 히스토그램의 최소오차값을 minError[i][N]에 저장
		for j in range(1, n+1):
			for k in range(1, j): # 마지막 그룹이 [k .. j-1]일 경우
				minError[i][j] = min(minError[i][j], minError[i-1][k] + mse(k+1, j))
	return minError[B][n]
'''start of main'''
B, n = map(int, input().split())
dp1 = [0]*(n+1) #dp1[k]는 A[0] ~ A[k]까지 수의 합이 저장됨 -> A[3] + A[4] + A[5] = dp1[5] - dp1[2]
dp2 = [0]*(n+1) #dp2[k]는 A[0]^2 ~ A[k]^2 까지 수의 합이 저장됨 -> A[3]^2 + A[4]^2 + A[5]^2 = dp2[5] - dp2[2]
# A = [4, 2, 3, 6, 5, 6, 12, 16]
for i in range(1, n+1):
	int_input = int(sys.stdin.readline().rstrip())
	dp1[i] = dp1[i-1] + int_input #[0, 4, 6, 9, 15, 20, 26, 38, 54] -> 계산의 편의상 0인덱스값을 0으로 합니다
	dp2[i] = dp2[i-1] + int_input*int_input #[0, 16, 20, 29, 65, 90, 126, 270, 526] -> ''
minError = [[math.inf]*(n+1) for _ in range(B+1)] #minError[i][j] = 1부터 j-1까지 범위에서 i개의 그룹으로 만들어지는 히스토그램의 최소오차
for i in range(1, n+1): # 그룹이 1개일때 minError 초기화
	minError[1][i] = mse(1, i)
print(round(solve(B, n), 3))
'''end of main'''

'''
<알고리즘 설명>
오차를 구하는 식을 정리하면 A = [a, b, c]가 있을 때
평균 m = (a+b+c)/3
mse = (m-a)^2 + (m-b)^2 + (m-c)^2 = a^2 + b^2 + c^2 -2m(a+b+c) + 3m^2, 여기서 (a+b+c) = 3m이므로
풀어쓰면 mse = (a^2 + b^2 + c^2) - 3m^2 = (a^2 + b^2 + c^2) - {(a + b + c)^2}/3
이렇기 때문에 만약 각 원소의 제곱의 축적합(dp2) 그리고 각 원소의 축적합(dp1)을 미리 알고 있다면
해당 구간에서 상수시간에 mse를 구할 수 있습니다. 예를 들어
a=A[1], b = A[2], c = A[3]라고 하면 -> MSE = (dp2[3] - dp2[0]) - (dp1[3] - dp1[0])*(dp1[3] - dp1[0])/(3-1+1)
왜냐하면
dp1[k]는 A[0] ~ A[k]까지 수의 합이 저장됨 -> A[3] + A[4] + A[5] = dp1[5] - dp1[2]
dp2[k]는 A[0]^2 ~ A[k]^2까지 수의 합이 저장됨 -> A[3]^2 + A[4]^2 + A[5]^2 = dp2[5] - dp2[2]

자신의 위치 j에서 현재 그룹이 i개 일때, i-1개 그룹일때 j-1까지의 최소오차값 중에서 j를 포함한 i개의 그룹을 구성했을때의 만들어지는 히스토그램의 최소오차값을 minError[i][j]에 저장합니다
minError[i][j] = min(minError[i][j], minError[i-1][k] + mse(k+1, j)) (k는 1 to j-1)

<수행시간 분석>
그룹의 최대 개수를 B, 총 빈도수의 개수를 n 이라고 하면
mse를 빠르게 구하기 위해 필요한 dp1, dp2를 채워넣을때 걸리는 시간 -> O(c*n) = O(n)
i 개의 그룹일때 해당 그룹으로 만들어지는 히스토그램의 최소오차값 minError에 저장하는 시간을 구하면
그룹이 1개일 때 minError의 경우 -> O(n)
그룹이 2개 이상일때 minError의 경우 위의 solve함수를 보면 i는 2 to B까지 가고,
각 그룹의 개수(i)일 때마다 j는 1 to n까지, k는 1 to j-1까지 이므로
그룹이 i개 일 때 minError를 채우는데 걸리는 시간은 c*(0 + 1 + 2 + ... + n-1) = O(c*n^2)이 되기 때문에 결과적으로 그룹이 B개일 때 까지 실행하야 하므로 결과적으로 -> O(c*(B-1)*n^2) = O(B*n^2)
=> 총 수행시간: O(B*n^2)
'''
