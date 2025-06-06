# m - x 좌표, n - y 좌표

def solution(m, n, puddles):

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            
            if [j+1, i+1] in puddles:
                continue

            if i == 0 and j != 0:
                dp[i][j] += dp[i][j-1]
            elif i != 0 and j == 0:
                dp[i][j] += dp[i-1][j]
            elif i != 0 and j != 0:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    return dp[n-1][m-1] % 1000000007