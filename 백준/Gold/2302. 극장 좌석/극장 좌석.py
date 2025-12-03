n = int(input())
arr = []
for _ in range(int(input())):
    arr.append(int(input()))

part = []
cnt = 0
for i in range(1, n+1):
    if i in arr:
        part.append(cnt)
        cnt = 0
    else:
        cnt += 1     
part.append(cnt)

l = max(part)
if l == 1:
    dp = [0, 1]
elif l == 2:
    dp = [0, 1, 2]
elif l > 2:
    dp = [0] * (l+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, l+1):
        dp[i] = dp[i-2] + dp[i-1]

ans = 1
for n in part:
    if n != 0:
        ans *= dp[n]

print(ans)