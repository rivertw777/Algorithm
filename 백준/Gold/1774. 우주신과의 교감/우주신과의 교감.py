import sys
import math
input = sys.stdin.readline


N, M = map(int, input().split())
dots = []
edges = []
parent = [i for i in range(N+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    minP, maxP = min(a, b), max(a, b)
    parent[maxP] = minP


for _ in range(N):  # 정점
    x, y = map(int, input().split())
    dots.append((x, y))

for _ in range(M):  # 이미 연결된 간선
    a, b = map(int, input().split())
    union(a, b)

# 가능한 모든 간선 구하기
for i in range(N):
    for j in range(i+1, N):
        if find(i+1) != find(j+1):  # (주의)연결되어 있지 않을 때
            edges.append((math.sqrt((dots[i][0]-dots[j][0])**2 + (dots[i][1]-dots[j][1])**2), i+1, j+1))  # (비용, 점a , 점b)

edges.sort()  # 간선 비용 오름차순 정렬
result = 0
# print(edges)

for w, a, b in edges:  # 최소 간선부터 모든 노드가 연결 될 때까지 반복
    if find(a) != find(b):
        union(a, b)
        result += w

print("{:.2f}".format(result))  # (주의) 4.0이라도 4.00으로 나오도록 출력
