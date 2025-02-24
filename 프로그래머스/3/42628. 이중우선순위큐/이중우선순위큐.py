import heapq as hq

def solution(op):
    p = []
    hq.heapify(p)
    
    for i in op:
        a, b = i.split(" ")
        
        if a == "I":
            hq.heappush(p, int(b))
        elif p and a == "D" and b == "-1":
            hq.heappop(p)
        elif p and a == "D" and b == "1":
            p.remove(max(p))
    
    if p: 
        return [max(p), min(p)]
    else:
        return [0, 0]