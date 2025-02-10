import heapq as hq

def solution(n, costs):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n
    p = []
    
    for a, b, cost in costs:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    hq.heappush(p, (0,0))
    
    while False in visited:
        cost, now = hq.heappop(p)
        
        if visited[now] == True:
            continue
        
        visited[now] = True
        answer += cost
        for end, cost in graph[now]:
            if visited[end] == False:
                hq.heappush(p, (cost, end))
        
    return answer