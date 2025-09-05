import sys
input = sys.stdin.readline

# Union-Find 알고리즘
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    x = find(x)
    y = find(y)

    if x <= y:
        parent[y] = x
    else:
        parent[x] = y

# 거리 계산
def dist(star1,star2):
    x1,y1 = star1
    x2,y2 = star2
    return round(((x1-x2)**2+(y1-y2)**2)**0.5, 2)

n = int(input())
nodes = [list(map(float,input().split())) for _ in range(n)]
edges = []
parent = list(range(n))
res = 0
for i in range(n):
    for j in range(i+1,n):
        d = dist(nodes[i],nodes[j])
        edges.append((d,i,j))
        
# 간선을 최소 비용 순으로 정렬
edges.sort(key = lambda x: x[0])

for i in range(len(edges)):
    d,x,y = edges[i]
    if find(x) != find(y): # 부모가 다르면
        union(x,y) # 최소 신장트리에 포함시킴
        res += d

print(res)