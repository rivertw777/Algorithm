def dfs(v, graph, visited):
    visited[v] = True
    count = 1  # 현재 노드 카운트
    for u in graph[v]:
        if not visited[u]:
            count += dfs(u, graph, visited)
    return count

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for v, u in wires:
        graph[v].append(u)
        graph[u].append(v)

    answer = 100
    for i in range(n - 1):
        visited = [False for _ in range(n + 1)]
        v1, v2 = wires[i]
        visited[v2] = True
        tmp = abs(dfs(v1, graph, visited) - dfs(v2, graph, visited))
        answer = min(tmp, answer)

    return answer