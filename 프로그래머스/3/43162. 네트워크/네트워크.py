from collections import deque

def bfs(i, computers, visited):
    q = deque([i])

    while q:
        item = q.popleft()
        visited[item] = True
        
        for n in range(len(computers)):
            if not visited[n] and computers[item][n] == 1:
                q.append(n)

def solution(n, computers):
    answer = 0

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1
    
    return answer