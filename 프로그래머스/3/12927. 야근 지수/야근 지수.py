import heapq as hq

def solution(n, works):
    
    q = []
    for i in works:
        hq.heappush(q, -i)
    
    for _ in range(n):
        item = hq.heappop(q)

        if item + 1 != 0:
            hq.heappush(q, item + 1)
        
        if not q:
            break
                        
    answer = 0
    for i in q:
        answer += i * i
    return answer