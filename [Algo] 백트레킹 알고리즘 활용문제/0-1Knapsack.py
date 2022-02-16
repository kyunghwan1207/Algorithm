def frac_knapsack(i, size):
	'''
	입력: 
    	i: 선택해서 배낭에 넣을 노드번호
		size: 배낭의 남은 용량
	출력:
		i번째 노드를 선택해서 배낭에 넣었을때 예상되는 최대이익
	'''
	pass
	
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


