import heapq as hq

def solution(op):
    
    q = []
    for i in op:
        a, b = i.split()
        if a == 'I':
            hq.heappush(q, int(b))
        elif a == 'D' and q:
            if b == '1':
                q.remove(max(q))
            elif b == '-1':
                hq.heappop(q)
    
    if q:
        return [max(q), min(q)]
    else:
        return [0,0]