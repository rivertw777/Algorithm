n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])

l = max(dp)
ans = []
for i in range(n-1, -1, -1):    
    if dp[i] == l:
        ans.append(arr[i])
        l -= 1

print(max(dp))
for i in ans[::-1]:
    print(i, end=' ')