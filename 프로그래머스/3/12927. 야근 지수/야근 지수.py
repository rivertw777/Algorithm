import heapq as hq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    max_heap = [-work for work in works]
    hq.heapify(max_heap)
    
    for _ in range(n):
        max_work = hq.heappop(max_heap)
        hq.heappush(max_heap, max_work + 1)
    
    ans = 0
    for i in max_heap:
        ans += i ** 2
        
    return ans