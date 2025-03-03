import heapq as hq

def solution(jobs):
    n = len(jobs)
    jobs.sort()
    
    answer = 0
    time = 0
    q = []
    while jobs or q:
        while jobs and jobs[0][0] <= time:
            hq.heappush(q, jobs.pop(0)[::-1])
        
        if q:
            item = hq.heappop(q)
            time += item[0]
            answer += ( time - item[1] )
            
        else:
            time = jobs[0][0]
                    
    return answer // n