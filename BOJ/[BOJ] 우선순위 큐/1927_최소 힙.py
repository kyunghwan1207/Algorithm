import heapq
import sys
input = sys.stdin.readline

n = int(input())
H = [] # heaq.heapify()
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(H) != 0:
            print(heapq.heappop(H))
        else:
            print(0)
    else:
        heapq.heappush(H, x)

'''
<알고리즘 설명>
n개의 수를 입력받으면서 x의 값에 따라서 우선순위 큐(H)에 적절한 연산을 수행합니다.
x가 0일 경우엔, 최소값(루트에 있는 값)을 출력(heappop)하고,
x가 0이 아닐 경우엔, 우선순위 큐(H)에 값을 넣는(heappush) 연산을 수행합니다.

<수행시간 분석>
우선순위 큐(H)의 원소의 개수를 n이라고 가정하겠습니다.
heappop연산의 경우 루트의 있는값을 꺼내고 이진트리의 맨 마지막에 있는 원소를 루트로 가져와서 
다시 우선순위 큐의 셩질(heap property)을 만족시키기 위한(heapify)연산을 수행합니다. -> O(log n)
heappush연산의 경우 이진트리의 맨 마지막에 원소를 추가하고 heap property를 만족시키기 위해 heapify연산을 수행 -> O(log n)
=> 총 수행시간: O(n*log n)
'''