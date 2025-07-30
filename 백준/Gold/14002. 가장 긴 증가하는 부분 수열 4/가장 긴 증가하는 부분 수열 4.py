n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
       
        if dp[i] == 0:
            dp[i] = 1

answer = []
big = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == big:
        answer.append(arr[i])
        big -= 1

print(max(dp))
for i in answer[::-1]:
    print(i, end=' ')