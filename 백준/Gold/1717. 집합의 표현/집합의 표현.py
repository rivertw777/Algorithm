import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) 

n, m = map(int, input().split())
parent = [i for i in range(n+1)] 

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: # 더작은 쪽이 부모
        parent[b] = a
    else:
        parent[a] = b
    
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(m):
    k, a, b = map(int, input().split())

    if k == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("yes")
        else:
            print("no")