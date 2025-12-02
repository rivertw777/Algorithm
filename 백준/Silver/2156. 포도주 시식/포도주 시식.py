n = int(input())
wine = []
for i in range(n):
    wine.append(int(input()))

if n == 1: print(wine[0])
elif n == 2: print(wine[0] + wine[1])
else:
    dp = [0] * n
    
    dp[0] = wine[0]
    dp[1] = wine[0]+wine[1]

    # 2번째 + 3번째 or 1번째 + 3번째 or 1번째 + 2번째 
    dp[2] = max(wine[1]+wine[2], wine[0]+wine[2], wine[0]+wine[1])

    for i in range(3, n):
        # dX or dXOO or dXO
        dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])

    print(dp[n-1])