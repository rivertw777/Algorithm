import sys
input = sys.stdin.readline

N = int(input())

f = [[0]*(N+1) for i in range(20)]
data = [*map(int,input().split())]
for i in range(N):
  f[0][i+1] = data[i]

for i in range(1,20):
  for n in range(1,N+1):
    f[i][n] = f[i-1][f[i-1][n]]

Q = int(input())
for _ in range(Q):
  n,x = map(int,input().split())
  for i in range(20):
    if n&(1<<i):
      x = f[i][x]
  print(x)