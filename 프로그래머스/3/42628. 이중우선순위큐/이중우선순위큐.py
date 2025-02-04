import heapq as hq

def solution(operations):
    answer = []
    
    q = []
    for op in operations:
        a, b = op.split(" ")
        
        if q and a == "D" and b == "1":
            q.remove(max(q))
        elif q and a == "D" and b == "-1":
            hq.heappop(q)
        elif a == "I":
            hq.heappush(q, int(b))
                            
    if q:
        return [max(q), min(q)]
    else:
        return [0,0]