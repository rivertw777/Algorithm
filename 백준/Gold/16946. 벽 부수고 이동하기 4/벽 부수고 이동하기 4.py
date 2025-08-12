from collections import deque

def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        zeros[x][y] = group
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if not graph[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

def move_count(x, y):
    data = set()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not zeros[nx][ny]:
            continue
        data.add(zeros[nx][ny])
    cnt = 1
    for c in data:
        cnt += info[c]
        cnt %= 10
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
zeros = [[0] * m for _ in range(n)]
answer = [[0] * m for _ in range(n)]

group = 1
info = {}

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(m):
        if not graph[i][j] and not visited[i][j]:
            cnt = bfs(i, j)
            info[group] = cnt
            group += 1

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            answer[i][j] = move_count(i, j)

for i in range(n):
    print("".join(map(str, answer[i])))