import sys
input = sys.stdin.readline

# 유니온 파인드

def find(x):
    if graph[x] < 0:
        return x
        
    graph[x] = find(graph[x])
    return graph[x]
    
def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    if graph[x] < graph[y]:
        graph[y] = x
    elif graph[y] < graph[x]:
        graph[x] = y
    else:
        graph[x] = y
        graph[y] -= 1
        
    return

N = int(input())
M = int(input())
graph = [-1]*(N+1)

# 연결 관계가 1인 두 노드의 루트 노드를 합쳐준다.(그래프 합치기)
for start in range(1, N+1):
    for end, isLinked in zip(range(1, N+1), map(int, input().split())):
        if isLinked:
            union(start, end)
   
path = list(set(map(int, input().split())))
result = "YES"
# 방문 경로 내 도시 중, 한 쌍이라도 루트 노드가 서로 다르다면
# 즉, 서로가 한 그래프 내에 존재하지 않는다면 방문 경로는
# 절대로 다 돌 수 없으므로 result = "NO"
# 한 편, len(path)가 1인 경우는 그냥 그 도시만 방문하면되니까
# YES 출력
for i in range(1, len(path)):
    if find(path[0]) != find(path[i]):
        result = "NO"
        break
print(result)