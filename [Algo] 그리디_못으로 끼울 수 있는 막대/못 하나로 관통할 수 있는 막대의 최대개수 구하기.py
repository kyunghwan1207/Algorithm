import sys
import heapq
n = int(sys.stdin.readline())
L = []
for _ in range(n):
	a, b = map(int, sys.stdin.readline().split())
	L.append([a, b])
L.sort(key=lambda x : [x[0], x[1]]) # a기준 오름차순 정렬 후 b기준으로 오름차순 정렬 => O(nlogn)
# [시작점(a), 끝점(b)] 형태로 저장되고
# L은 a기준으로 오름차순 정렬하고 만약 a가 동일하면 b에 대해서 오름차순정렬합니다.
F = [] # 끝나는 점 모음
#heapq.heapify(F) # minHeap
heapq.heappush(F, L[0][1])
cnt = 1 # 최대로 겹치는 막대갯수
for i in range(1, n):
	if F[0] < L[i][0]:
		heapq.heappop(F)
	heapq.heappush(F, L[i][1])
	cnt = max(cnt, len(F))
print(cnt)