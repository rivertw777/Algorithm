import heapq as hq

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [10e9] * (n + 1) 
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q = []
    hq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, cur = hq.heappop(q)
        
        if dist > distance[cur]:
            continue
        
        for i in graph[cur]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                hq.heappush(q, (cost, i))
        
    m = max(distance[1:])
    cnt = 0
    for i in distance:
        if i == m:
            cnt += 1
    return cnt