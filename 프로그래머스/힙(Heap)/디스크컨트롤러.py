import heapq

def solution(jobs):
    answer = 0
    H = []
    n = len(jobs)
    cnt = n
    curr_time = 0

    while cnt:
        for i in range(len(jobs)):
            if jobs[i][0] <= curr_time:
                heapq.heappush(H, [jobs[i][1], jobs[i][0], i])
        if len(H) == 0:
            curr_time += 1
            continue
        take, start, idx = heapq.heappop(H)
        answer += curr_time + take - start
        curr_time += take
        jobs.pop(idx)

        cnt -= 1
        H = []
        
    return answer // n
