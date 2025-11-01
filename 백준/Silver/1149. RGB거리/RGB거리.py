n = int(input())

home = []
for _ in range(n):
    home.append( list(map(int, input().split())) )

dp = [[0 for _ in range(n)] for _ in range(3)]

dp[0][0] = home[0][0]
dp[1][0] = home[0][1]
dp[2][0] = home[0][2]

for i in range(1, n):
    
    dp[0][i] = home[i][0] + min(dp[1][i-1], dp[2][i-1]) 
    dp[1][i] = home[i][1] + min(dp[0][i-1], dp[2][i-1])
    dp[2][i] = home[i][2] + min(dp[0][i-1], dp[1][i-1])

print( min(dp[0][-1], dp[1][-1], dp[2][-1]) )