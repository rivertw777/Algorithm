n = int(input())

t = []
p = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    
    # 남은 일자가 부족하다면 pass
    if i + t[i] > n: 
        dp[i] = dp[i+1]
    # i일에 상담 안하는 것과 상담하는 것 중 비교
    else:
        dp[i] = max(dp[i+1], dp[i + t[i]] + p[i])

print(max(dp))