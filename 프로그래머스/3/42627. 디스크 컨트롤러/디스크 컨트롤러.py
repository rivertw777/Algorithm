import heapq as hq

def solution(jobs):
    n = len(jobs)
    jobs.sort()
    
    q = []
    cur = 0
    total = 0
    while q or jobs:
        
        while jobs and cur >= jobs[0][0]: #  현재 시점 넣을 수 있는 작업 모두 삽입
            hq.heappush(q, jobs.pop(0)[::-1])
            
        if q:
            job = hq.heappop(q)[::-1]
            cur += job[1]
            total += cur - job[0]
        else:
            cur = jobs[0][0]
                        
    return total // n