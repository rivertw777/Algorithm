from collections import deque

def bfs(start, computers, visited):
    visited[start] = True
    q = deque([start])
    while q:
        cur = q.popleft()
        for i in range(len(computers[cur])):            
            if i != cur and computers[cur][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
            
def solution(n, computers):
    answer = 0
    visited = [False] * n
 
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1
        
    return answer