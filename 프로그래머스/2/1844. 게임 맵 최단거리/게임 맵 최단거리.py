from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
        
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    q = deque([(0,0)])
    while q:
        item = q.popleft()
        x, y = item[0], item[1]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
                
            if maps[nx][ny] != 0 and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                
                if maps[-1][-1] != 1:
                    return maps[-1][-1]
                
    return -1