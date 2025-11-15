n = int(input())
array = list(map(int, input().split()))

dp = [1] * n
dp[0] = array[0]
for i in range(1, n):
  for j in range(i):
    if array[j] < array[i]: # 앞에 원소가 뒤에 원소보다 작을 경우 
      dp[i] = max(dp[i], dp[j] + array[i]) 
    else:
      dp[i] = max(dp[i], array[i])

print(max(dp))