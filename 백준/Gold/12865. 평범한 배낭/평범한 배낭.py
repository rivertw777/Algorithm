n, k = map(int, input().split())

item = []
for i in range(n):
    w, v  = map(int, input().split())
    item.append((w, v))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1): 
    for j in range(1, k+1):
        if j >= item[i-1][0]:  
            dp[i][j] = max(item[i-1][1] + dp[i-1][j-item[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[n][k]) 