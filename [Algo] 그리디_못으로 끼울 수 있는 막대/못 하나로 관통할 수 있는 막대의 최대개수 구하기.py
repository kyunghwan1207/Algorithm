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
'''
<알고리즘 설명>
현재의 문제는 최대로 많이 겹치는 막대의 개수를 구하는 것이기에 끝점을 기준으로 봤을때 
"끝점 >= 시작점"인 막대들은 겹치는 막대이고
"끝점 < 시작점"인 막대는 안 겹치는 막대이다. 
따라서 막대가 겹치지 않을때 만 pop하고 나머지는 계속 push하다 보면 len(minHeap)은 겹치는 막대의
개수가 됩니다. 그중 cnt에 max를 유지하면서 n-1까지 순회하고 최종 cnt값(=끝점 기준 겹치는 막대의 최대갯수)을 출력합니다.
Step 1. 시작점을 기준으로 오름차순 정렬한 후 끝점을 기준으로 오름차순 정렬합니다. 
Step 2. minHeap인 F를 통해 현재까지 겹치는 막대들의 끝점을 저장해서 유지기때문에 
len(F)는 현재까지 겹치는 막대들의 개수이고
이 값을 통해 cnt를 제일 큰값으로 유지합니다.
만약 Step 2에서 현재의 끝점(F[0]) 보다 큰 시작점을 가진 막대를 만나면 더이상 겹치지 않기때문에 minHeap에서 pop합니다.
새롭게 겹치는 막대들을 minHeap에 저장해갑니다. 어차피 cnt에는 최대값이 유지되므로 
결과적으로 cnt에는 최대로 겹치는 막대의 개수가 저장됩니다.


<수행시간 분석>
막대의 개수를 n이라고 하면
Step 0. a와 b 입력받음 -> O(n)
Step 1 -> O(nlogn)

A의 크기가 n일 때, heapq.heappop(A)연산은 min값(=root노드)를 pop하고(즉, A[0])를 꺼내고( O(1) ) 
A[n-1]번째 노드를 root에 배치 시킨 후 다시 heap-property를 만족하도록 비교와 swap연산을 반복합니다.(heapify_down연산)
이때 heapify_down연산의 수행시간은 힙의 높이를 h라고 하면 O(h)만큼의 시간이 걸립니다. 따라서 heap-property를 만족하도록
부모노드가 자식노드와 비교 및 swap연산을 통해 한 level씩 내려갈때 마다 비교 대상이 절반씩 감소하는 것이므로 
O(h) = O(logn)이 됩니다.
(heap은 완전 이진트리로 구현되었기 때문) 따라서 heapq.heappop(A) -> O(logn)

A의 크기가 n일 때, 
heapify_down은 트리의 높이만큼의 수행시간이 필요하기 떄문에 O(logn)이 소모됩니다. 따라서
A의 크기가 n일 때, heapq.heappush(A, k)의 수행시간은 원소추가(append)하고, heapify_down 수행하는 것이므로 O(logn)
A의 크기가 n일 때, heapq.heappop(A)의 수행시간은 원소를 swap하고, 지우고(pop), heapify_down 수행하는 것이므로 O(logn)의 수행시간이 걸립니다.

Step 2 -> n * (heappush연산 + heappop연산 + c) = O(nlogn)

최종수행시간 => O(nlogn)
'''
