import heapq
def solve(A, k): # return k-th smallest key, 1 <= k <= n
	'''k번째로 작은 수 찾기_(k-1번 pop한 다음 A[0]를 보면 k번째로 작은 수이다.)'''
	for _ in range(k-1):     #k-1번 반복
		heapq.heappop(A)       #O(logn)
	return A[0]
#총 수행시간: O((k-1)*logn) = O(k*logn)
k = int(input())
A = [int(x) for x in input().split()]
heapq.heapify(A) # A is now a min-heap
print(solve(A, k))
'''
<수행시간 분석>
조건: 
1. 리스트 A의 크기는 n이라고 가정
2. for 반복문을 제어하는 연산은 수행시간 고려대상에서 제외함.

리스트 A의 값을 min힙으로 만드는 시간 -> O(n)
heapq.heappop(A)연산은 min값(=root노드)을 pop하고(즉, A[0]를 꺼내고)( O(1) ) A[n-1]번째 노드를 root에 배치 시킨 후 다시 heap-property를 만족하도록 비교와 swap 연산을 반복한다. 이때 수행시간은 힙의 높이를 h라고 하면 O(h)만큼의 시간이 걸린다. 따라서 heap-property를 만족하도록 부모노드가 자식노드와 비교및 swap연산을 통해 한 level씩 내려갈때마다 비교 대상이 절반씩 감소하는 것이므로 O(h) = O(logn)이 된다.(heap은 완전 이진트리로 구현되었기 때문) -> O(logn)
이후 힙 성질을 이용해 k 번째로 작은 수를 찾을 것이다. 
이때 k번째로 작은 수 이므로 haeppop(A)( 앞서 애기한대로 O(logn) )를 k-1번 수행하고 난 다음 A[0]를 보면( O(1) )
k번째로 작은 수를 찾을 수 있다. 이때의 시간 -> O((k-1)*logn + 1) = O(k*logn)
따라서
전체적인 알고리즘의 흐름을 정리하면
리스트 A의 값을 min힙으로 만들고( O(n) ), solve(A, k)함수에서 리스트 A에서 k번째로 작은 수를 찾기 위해서 heappop(A)를 k-1번 수행하므로( O(k*logn) )
알고리즘의 총 수행시간 => O(n + k*logn)이 된다.

<세 가지 알고리즘과 비교해 나의 Algorithm_HEAP 알고리즘의 장-단점 기술>

[단점]
최악의 경우인 k가 n인 경우에는 시간복잡도가 O(nlogn)이 된다.
Algorithm_SORT에 비해 코드를 이해하기가 어렵다.
Algorithm_QUICK의 평균적인 경우에 비해 수행시간이 느리다.
Algorithm_MOM에 비해 수행시간이 느리다.

[장점]
최악의 경우를 제외하곤 O(nlogn) 미만의 시간 복잡도를 가진다.
최악의 경우가 아닌 경우에는 Algorithm_SORT에 비해 수행시간이 빠르다.(왜냐하면,Algorithm_SORT는 무조건 정렬을 해야하므로)
나의 알고리즘인 Algorithm_HEAP과 Algorithm_QUICK에서 서로같이 최악의 경우를 따졌을때
나의 알고리즘은 O(nlogn)인 반면 Algorithm_QUICK은 O(n^2)이므로
Algorithm_QUICK의 최악의 경우에 비해 수행시간이 빠르다.
Algorithm_MoM의 수행시간을 T(n)이라고 할때,
MoM 점화식 증명 부분을 보면 T(n) <= 60n이라고 나와있다.
따라서 숨겨진 상수가 커서 Algorithm_MoM의 실제 수행시간이 커져 만약 T(n) = 60n이라면
이러한 경우에선 실제 수행시간 측면에서 나의 Algorithm_HEAP이 더 빠르다고 할 수 있다.
'''