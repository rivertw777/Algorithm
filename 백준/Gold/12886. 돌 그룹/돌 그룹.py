from collections import deque

def bfs(stone):
    total = sum(stone)
    visited = [[False] * (total + 1) for _ in range(total + 1)]
    
    a, b = stone[0], stone[1]
    q = deque()
    q.append((a,b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        z = total - x - y

        if x == y == z:
            return 1

        for v1, v2 in [(x,y), (y,z), (z,x)]:
            if v1 > v2:
                v1, v2 = v2, v1
            v2 = v2 - v1
            v1 = 2 * v1
            v3 = total - v1 - v2
            v1, v2 = max(v1, v2, v3), min(v1, v2, v3)
            
            if not visited[v1][v2]:
                visited[v1][v2] = True
                q.append((v1, v2))

    return 0

stone = list(map(int,input().split()))

if sum(stone) % 3 != 0:
    print(0)
else:
    print(bfs(sorted(stone)))