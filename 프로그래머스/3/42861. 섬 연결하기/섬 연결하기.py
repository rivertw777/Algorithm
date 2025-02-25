import heapq as hq

def solution(n, costs):
    graph = [[] for _ in range(n)]
    visited = [False] * n
    p = []
    
    for a, b, cost in costs:
        graph[a].append([b, cost])
        graph[b].append([a, cost])
            
    ans = 0
    hq.heappush(p, (0,0))
    while False in visited:
        cost, cur = hq.heappop(p)
        
        if visited[cur]:
            continue
        
        visited[cur] = True
        ans += cost
        for node, cost in graph[cur]:
            if not visited[node]:
                hq.heappush(p, (cost, node))

    return ans