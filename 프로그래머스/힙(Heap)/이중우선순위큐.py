import heapq

def solution(operations):
    answer = [0, 0]
    H = []
    H_temp = []
    for op in operations:
        cmd, num = op.split()
        if cmd == "I":
            heapq.heappush(H, int(num))
        elif num == "1":
            if len(H) == 0: continue
            for _ in range(len(H)-1):
                heapq.heappush(H_temp, heapq.heappop(H))
            heapq.heappop(H) # 최댓값 삭제
            for _ in range(len(H_temp)):
                heapq.heappush(H, heapq.heappop(H_temp))
        else:
            if len(H) == 0: continue
            heapq.heappop(H) # 최솟값 삭제
    if len(H) != 0:
        answer[1] = heapq.heappop(H)
        for _ in range(len(H) - 1):
            heapq.heappop(H)
        answer[0] = heapq.heappop(H)
    return answer
