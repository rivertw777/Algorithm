import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

USE, NOT_USE = 0, 1

def solve(node, used):
    if dp[node][used][0] != 0:
        return dp[node][used]

    if used == USE:
        ans = weights[node]
        combi = [node]
        for conn_node in graph[node]:
            if visit[conn_node]:
                continue
            visit[conn_node] = True
            _ans, _combi = solve(conn_node, NOT_USE)
            ans += _ans
            combi += _combi

    else:
        ans = 0
        combi = []
        for conn_node in graph[node]:
            if visit[conn_node]:
                continue
            visit[conn_node] = True
            _ans1, _combi1 = solve(conn_node, USE)
            visit[conn_node] = True
            _ans2, _combi2 = solve(conn_node, NOT_USE)
            if _ans1 > _ans2:
                ans += _ans1
                combi += _combi1
            else:
                ans += _ans2
                combi += _combi2

    dp[node][used] = (ans, tuple(combi))
    visit[node] = False
    return dp[node][used]



n = int(input())
graph = [[] for _ in range(n+1)]
weights = [0] + list(map(int, input().split()))
visit = [False]*(n+1)
for _ in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dp = [[(0, tuple()), (0, tuple())] for _ in range(n+1)]
visit[1] = True
answer1, combi1 = solve(1, USE)
visit[1] = True
answer2, combi2 = solve(1, NOT_USE)
# 
# print(answer1, combi1)
# print(answer2, combi2)
if answer1 > answer2:
    print(answer1)
    print(*sorted(combi1))
else:
    print(answer2)
    print(*sorted(combi2))