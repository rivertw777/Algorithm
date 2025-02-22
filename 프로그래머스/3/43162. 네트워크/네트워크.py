from collections import deque

def bfs(start, computers, visited):
    q = deque([start])
    visited[start] = True
    
    while q:
        item = q.popleft()
        for i in range(len(computers[item])):
            if computers[item][i] != 0 and not visited[i]:
                visited[i] = True
                q.append(i)  
                

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1
        
    return answer