t = int(input())

for _ in range(t):
    n = int(input())
    
    if n == 1 or n == 2 or n == 3:
        print(1)

    else:
        dp  = [0] * n
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3, n):
            dp[i] = dp[i-3] + dp[i-2]
    
        print(dp[n-1])