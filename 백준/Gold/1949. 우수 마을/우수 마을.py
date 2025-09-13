import sys
sys.setrecursionlimit(10**6)

input = lambda : sys.stdin.readline().rstrip()
T = int(input())
population = dict(zip(range(1, T+1), list(map(int, input().split()))))

tree = [[] for _ in range(T+1)]
for _ in range(T-1):
    a, b = map(int, input().split())
    tree[b].append(a)
    tree[a].append(b)

visit = set()
dp = [[0] * (T+1) for _ in range(2)]
dp[1] = [0] + list(population.values())

def dfs(x):
    global visit, tree
    visit.add(x)
    for nx in tree[x]:
        if nx not in visit:
            dfs(nx)
            dp[0][x] += max(dp[0][nx], dp[1][nx])
            dp[1][x] += dp[0][nx]

dfs(1)
print(max(dp[i][1] for i in range(2)))