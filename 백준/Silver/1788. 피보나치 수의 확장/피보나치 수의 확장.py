# 입력
n = int(input())

# DP
# n이 양수일 때
if n > 0:
    cache = [0, 1]
    for i in range(2, n+1):
        cache.append((cache[i-1] + cache[i-2]) % 1000000000)
    print(1)  # 양수
    print(cache[n])

# n이 0일 때
elif n == 0:
    print(0)
    print(0)
    
# n이 음수일 때
# f(n-2) = f(n) - f(n-1)
else:
    cache = [1, 0]  # f(1), f(0)
    for i in range(-n):
        tmp = cache[i] - cache[i+1]
        if tmp < 0:
            tmp = -tmp % 1000000000
            cache.append(-tmp)
        else:
            cache.append(tmp % 1000000000)
    print(-1 if cache[-n+1] < 0 else 1)
    print(abs(cache[-n+1]))