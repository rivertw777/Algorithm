def turn(i):
    if i == -1:
        return 3
    elif i == 4:
        return 0
    return  i

#######
n = int(input())
k = int(input())
apple = []
for i in range(k):
    apple.append(list(map(int, input().split())))
l = int(input())
info = []
for i in range(l):
    a, b = list(input().split())
    info.append([int(a), b])
#########
    
graph = [[0] * (n) for _ in range(n)]
for i in apple:
    graph[i[0]-1][i[1]-1] = 7
        
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

body = [[0,0]]
x, y = 0, 0
graph[x][y] = 4
ti = 0
time = 0
while True:
    # 헤드 갱신
    x, y = x + dx[ti], y + dy[ti]
    
    if x < 0 or y < 0 or x >= n or y >= n or [x,y] in body:
        time += 1
        break
            
    if graph[x][y] != 7: # 사과 아니면 꼬리 제거
        i, j = body.pop(0)
        graph[i][j] = 0
    
    # body 갱신    
    body.append([x, y])
    graph[x][y] = 4     
                
    time += 1
    
    # 방향 갱신
    if info and time == info[0][0]:
        if info[0][1] == 'D':
            ti = turn(ti + 1)
        else:
            ti = turn(ti - 1)
        info.pop(0)
        
print(time)