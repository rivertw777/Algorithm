n = int(input())
dp = [10e9] * (n+1)
dp[n] = 0

while n > 1:
    dp[n-1] = min(dp[n-1], dp[n] + 1)
    
    if n % 3 == 0:
        dp[n//3] = min(dp[n//3], dp[n] + 1)
        
    if n % 2 == 0:
        dp[n//2] = min(dp[n//2], dp[n] + 1)

    n -= 1
        
print(dp[1])