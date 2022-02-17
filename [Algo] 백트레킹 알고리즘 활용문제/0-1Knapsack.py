# 이 함수는 한계함수로 사용되며, 
# 하는일은 해당 노드를 선택했을때 예상되는 최대이익을 fractional knapsack방식으로 계산하여 return함으로써 앞으로 더 선택할지 말지 판단을 최대한 빨리 할 수 있도록 도와줌. 
# -> 알고리즘 효율성 증가
def frac_knapsack(i, size):
	current_size, current_prof = 0, 0
	for j in range(i, n):
		if current_size + L[j][2] <= size:
			current_size += L[j][2] # L[j][2] == 가성비 기준으로 정렬했을때의 S[j]
			current_prof += L[j][1] # L[j][1] == 가성비 기준으로 정렬했을때의 P[j]
		else:
			current_prof += (size-current_size)*L[j][0]
			break
	return current_prof
	
def knapsack(i, size): 
	# 0부터 i-1까지는 뽐을지 말지 정했고 이제 i번째 노드를 뽑 o/x -> 1/0 정하면됨, size는 남은용량
	global MP
	if i >= n or size <= 0:
		#print(x)
		return
	p_v = 0 # 현재 까지 선택된 아이템의 이익의 합
	s_v = 0 # 현재 까지 선택된 아이템의 용량의 합
	for j in range(i):
		if x[j] == 1:
			p_v += L[j][1]
			s_v += L[j][2]
	# x[i] = 1이 가능한지 -> i번째 노드를 선택햐아할까? 결정
	if L[i][2] <= size: # x[i]의 크기 = L[i][2] (가성비 기준으로 내림차순한 것(L) 기준)
		B[i+1] = frac_knapsack(i+1, size-L[i][2])
		if p_v + L[i][1] + B[i+1] > MP:
			# Update MP
			MP = max(MP, p_v + L[i][1])
			x[i] = 1
			knapsack(i+1, size-L[i][2])
	# x[i] = 0이 가능한지 -> i번째 노드를 선택하지말까까? 결정
	B[i+1] = frac_knapsack(i+1, size)
	if p_v + B[i+1] > MP:
		x[i] = 0
		knapsack(i+1, size)

K = int(input())
n = int(input())
S = [int(x) for x in input().split()]
P = [int(y) for y in input().split()] 
L = []
for i in range(n):
	L.append([P[i] / S[i], P[i], S[i]])
L.sort(key= lambda x : [-x[0], x[2]]) # 가성비 기준 내림차순 -> O(nlogn) 이후 용량 적은게 먼저 오도록
MP = 0
x = [0]*n # 뽑 o/x -> 1/0 으로 표시
B = [0]*(n+1) # B[i+1]은 i+1 ... n-1까지 아이템을 조건에 맞게 잘 조합한 factional 방식의 최대 예상이익
knapsack(0, K)
print(int(MP))


