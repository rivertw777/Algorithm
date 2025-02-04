
import heapq as hq

def solution(scoville, k):
    answer = 0
    
    q = []
    
    for i in scoville:
        hq.heappush(q, i)
    
    count = 0
    while q:
        first = hq.heappop(q)
        
        if first >= k:
            return count
        
        if q:
            second = hq.heappop(q)
            new = first + (second * 2)
            count += 1
            hq.heappush(q, new)               
        else:
            break
                        
    return -1
