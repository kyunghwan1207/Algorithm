import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # min-heap구조로 만듦
    
    while len(scoville) >= 2 and scoville[0] < K:
        new_sco = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new_sco)
        answer += 1
        
    if scoville[0] < K:
        answer = -1
        
    return answer
