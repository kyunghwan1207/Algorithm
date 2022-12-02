import heapq
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    S = [] # curr_num보다 작은 수들을 max-heap으로 관리
    B = [] # curr_num보다 큰 수들을 min-heap으로 관리
    curr_num = -10001
    for i in range(1, n+1):
        num = int(input())
        pos = int(i/2 + 0.5) # 가운데 위치, 즉 pos번째 위치한 수를 curr_num으로 유지시킴
        if curr_num == -10001:
            curr_num = num
        elif num < curr_num:
            heapq.heappush(S, -num)
        elif num >= curr_num:
            heapq.heappush(B, num)

        if len(S) + 1 == pos:
            print(curr_num)
            continue
        elif len(S) >= pos:
            heapq.heappush(B, curr_num)
            curr_num = -heapq.heappop(S)
        elif len(S) < pos:
            heapq.heappush(S, -curr_num)
            curr_num = heapq.heappop(B)
        print(curr_num)
'''
느낀점
1. 가운데 값을 유지하기 위해서 현재 가운데 값(curr_num) 보다 작은 값, 큰 값을 각각 S, B에 나눠서 관리한다
2. 이때 S는 max-heap으로 관리해야 curr_num보다 더 작은 값이 입력으로 들어왔을 때 -hp.heappop(S)를 통해서
그 다음 curr_num을 빠르게 찾을 수 있기 때문
3. B는 min-heap으로 관리함
'''
