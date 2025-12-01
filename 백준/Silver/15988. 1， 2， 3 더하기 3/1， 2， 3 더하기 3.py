t = int(input())
arr = []
for i in range(t):
    arr.append(int(input()))

if max(arr) == 1:
    dp = [0, 1]
elif max(arr) == 2:
    dp = [0, 1, 2]
elif max(arr) == 3:
    dp = [0, 1, 2, 4]
else:
    MOD = 1000000009
    dp = [0] * (max(arr) + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, max(arr) + 1):
        dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % MOD 

        
for n in arr:
    print(dp[n])