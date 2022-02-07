import sys
n = int(sys.stdin.readline())
L = []
for _ in range(n):
	a, b = map(int, sys.stdin.readline().split())
	L.append([a, b])
L.sort(key=lambda x : [x[1], x[0]]) # b기준 정렬 후 a기준 정렬
S = []
F = []
for i in range(n):
	S.append(L[i][0])
	F.append(L[i][1])
k = L[0][1] # 가장최근 막대의 끝점을 저장
cnt = 1
for i in range(1, n):
	if k < S[i]:
		cnt += 1
		k = F[i]
print(cnt)