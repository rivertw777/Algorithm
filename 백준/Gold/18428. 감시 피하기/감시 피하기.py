def dfs(cnt):
    global flag

    if cnt == 3:
        if not bfs(): # 감시 실패
            flag = True 
            return
    else:
        for x in range(n):
            for y in range(n):
                if graph[x][y] == "X":
                    graph[x][y] = "O"
                    dfs(cnt + 1)
                    graph[x][y] = "X"

# bfs를 통해 감시
def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for t in teacher:
        for k in range(4): 
            nx, ny = t

            while 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == "O":
                    break

                if graph[nx][ny] == "S":  # 감시 성공
                    return True

                nx += dx[k]
                ny += dy[k]

    return False # 감시 실패

n = int(input())
flag = False
graph = []
teacher = []

for i in range(n):
    graph.append(list(map(str, input().split())))
    for j in range(n):
        if graph[i][j] == "T": 
            teacher.append([i, j])

dfs(0)

if flag: # 모든 감시 통과
    print("YES")
else: 
    print("NO")