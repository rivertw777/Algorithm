# 가장 먼 노드
import heapq as hq

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [10e9] * (n+1)
    
    for i in edge:
        a, b = i[0], i[1]
        graph[a].append((b,1))
        graph[b].append((a,1))
                
    q = []
    hq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, cur = hq.heappop(q)
        
        if dist > distance[cur]:
            continue
            
        for i in graph[cur]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q, (cost, i[0]))
    
    max_distance = 0 
    for i in range(1, len(distance)):
        if distance[i] != 10e9:
            max_distance = max(max_distance, distance[i])
            
    return distance.count(max_distance)