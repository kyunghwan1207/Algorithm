import sys, math
def mse(left, right):
	sum_squared_val = dp2[right] - dp2[left-1]
	sum_val = dp1[right] - dp1[left-1]
	return round(sum_squared_val - (sum_val*sum_val)/(right-left+1), 3)
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
print(solve(B, n))
'''end of main'''