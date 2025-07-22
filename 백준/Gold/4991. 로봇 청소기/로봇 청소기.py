from collections import deque
import sys
input = sys.stdin.readline
def makeGraph(R,C,position,arr)->list|int:
    graph = list()
    value = bfs(R,C,0,arr,position)
    for v in value:
        if v == -1:
            return list()
    graph.append(value)
    for i in range(1,len(position)):
        graph.append(bfs(R,C,i,arr,position))
    return graph

def bfs(R,C,idx,arr,position):
    dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
    check = [[-1] * C for _ in range(R)]
    sr,sc = position[idx]
    check[sr][sc] = 0
    que = deque()
    que.append((sr, sc))
    while que:
        r,c = que.popleft()
        ncnt = check[r][c] + 1
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C) or check[nr][nc] != -1 or arr[nr][nc]=='x':
                continue
            check[nr][nc] = ncnt
            que.append((nr, nc))
    value = list()
    for i in range(len(position)):
        r,c = position[i]
        value.append(check[r][c])
    return value

def recur(totalLength,beforeNode):
    global ans,graph,notVisit
    if len(notVisit) == 0:
        ans = min(ans,totalLength)
        return
    if totalLength >= ans:
        return
    for nextNode in list(notVisit):
        notVisit.remove(nextNode)
        recur(totalLength+graph[beforeNode][nextNode],nextNode)
        notVisit.add(nextNode)

while True:
    C,R = map(int,input().split())
    if not C and not R:break
    arr = [input().rstrip() for _ in range(R)]
    position = [()]
    for r in range(R):
        for c in range(C):
            match arr[r][c]:
                case '*':
                    position.append((r,c))
                case 'o':
                    position[0] = (r,c)
    graph = makeGraph(R,C,position,arr)
    if len(graph) == 0:
        print(-1)
        continue
    ans = float('inf')
    notVisit = set(range(1,len(position)))
    recur(0,0)
    print(ans)