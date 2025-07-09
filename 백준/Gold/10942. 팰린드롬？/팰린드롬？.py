import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
d = [[0]*n for _ in range(n)]
for i in range(n):
    for start in range(n-i):
        end = start + i
        # 문자수 1개 : 시작점과 끝점이 같으므로 팰린드롬
        if start == end:
            d[start][end] = 1
        elif arr[start] == arr[end]:
            # 문자수 2개 : 시작 문자와 끝 문자가 같으면 팰린드롬
            if start+1 == end:
                d[start][end] = 1
            # 문자수 3개 이상 : 시작 문자와 끝 문자가 같고, 
            # 시작 문자와 끝 문자를 뺀 가운데 문자열이 팰린드롬이면 팰린드롬
            elif d[start+1][end-1] == 1:
                d[start][end] = 1

m = int(input())
for _ in range(m):
    s,e = map(int, input().split())
    print(d[s-1][e-1])