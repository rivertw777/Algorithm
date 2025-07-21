import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        graph[b].append(a)

    n1, n2 = list(map(int, input().split()))

    ans_list = [] # n1이 부모로 가질 수 있는 리스트

    nxt = n1
    while nxt != 0:
        ans_list.append(nxt)

        if len(graph[nxt]) == 0:
            nxt = 0
        else:
            nxt = graph[nxt][0]

    nxt = n2
    while nxt != 0:
        if nxt in ans_list:
            print(nxt)
            break

        if len(graph[nxt]) == 0:
            nxt = 0
        else:
            nxt = graph[nxt][0]