n = int(input())
dp = [10e9] * (n+1)
dp[n] = 0

while n > 1:
    dp[n-1] = min(dp[n-1], dp[n] + 1)
    
    if n % 3 == 0:
        n //= 3
        dp[n] = min(dp[n], dp[n*3] + 1)
        n *= 3
        
    if n % 2 == 0:
        n //= 2 
        dp[n] = min(dp[n], dp[n*2] + 1)
        n *= 2 

    n -= 1
        
print(dp[1])