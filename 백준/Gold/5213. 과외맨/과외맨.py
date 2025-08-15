from collections import deque
import sys

arr = []
n = int(sys.stdin.readline())
for h in range(n):
    row = []
    if not h % 2:
        for _ in range(n):
            row.extend(list(map(int, sys.stdin.readline().split())))
    else:
        for _ in range(n-1):
            row.extend(list(map(int, sys.stdin.readline().split())))
        row = [0] + row + [0]
    arr.append(row)

tile = [[-1] * 2 * n for _ in range(n)]
count = 1
for h in range(n):
    temp = 0
    for w in range(2*n):
        if h%2 and (w == 0 or w == 2*n-1):
            continue
        else:
            tile[h][w] = count
            temp +=1 

        if temp == 2:
            count += 1
            temp = 0

dire = [(1,0), (0, 1), (-1, 0), (0, -1)]
inf = 1e6
visit = [[1e9] * 2 * n for _ in range(n)]
visit[0][0] = 1

trace = [[(-1, -1)] * 2 * n for _ in range(n)]
trace[0][0] = (0, 0)

max_tile, max_tile_loc = -1, (0,0)
q = deque([(0,0)])
while q:
    x, y = q.popleft()
    t = visit[y][x]

    for dx, dy in dire:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 2*n and 0 <= ny < n:
            if tile[y][x] == tile[ny][nx] and t < visit[ny][nx]:
                q.append((nx, ny))
                visit[ny][nx] = t
                trace[ny][nx] = (x, y)
                if max_tile < tile[ny][nx]:
                    max_tile = tile[ny][nx]
                    max_tile_loc = (nx, ny)
            else:
                if arr[y][x] == arr[ny][nx] and t+1 < visit[ny][nx]:
                    q.append((nx, ny))
                    visit[ny][nx] = t+1
                    trace[ny][nx] = (x, y)
                    if max_tile < tile[ny][nx]:
                        max_tile = tile[ny][nx]
                        max_tile_loc = (nx, ny)


def path(a, b):
    ans = [tile[b][a]]
    x, y = trace[b][a]
    while True:
        if tile[y][x] == 1:
            ans.append(tile[y][x])
            break
        if tile[y][x] != ans[-1]:
            ans.append(tile[y][x])
        x, y = trace[y][x]
    return ans[::-1]

a, b = max_tile_loc
answer = path(a, b)
print(len(answer))
print(*answer)