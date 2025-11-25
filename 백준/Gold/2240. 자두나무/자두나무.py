t, w = map(int, input().split())
loc = [0] + [int(input()) for _ in range(t)]
dp = [[0] * (w + 1) for _ in range(t + 1)]

dp[1][0], dp[1][1] = loc[1] % 2, loc[1] // 2
for t in range(2, t + 1):
    for w in range(w + 1):
        j = loc[t] % 2 if w % 2 == 0 else loc[t] // 2
        dp[t][w] = max(dp[t-1][0:w+1]) + j

print(max(dp[-1]))