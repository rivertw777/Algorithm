# n - 총 지역 수
# roads - 길 정보
# sources - 각 부대원이 위치한 서로 다른 지역
# destination - 부대 지역

import heapq as hq

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n+1)]
    distance = [10e9] * (n+1)
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    q = []
    hq.heappush(q, (0, destination))
    distance[destination] = 0 
    while q:
        dist, cur = hq.heappop(q)
        
        if dist > distance[cur]:
            continue
        
        for i in graph[cur]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                hq.heappush(q, (cost, i))
    
    answer = []
    for i in sources:
        if distance[i] == 10e9:
            answer.append(-1)
        else:
            answer.append(distance[i])        
    return answer