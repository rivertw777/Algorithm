import math

N, K = map(int, input().split())
MOD = 1000000007

def mod_inv(a, p):
    # a의 p에 대한 모듈러 역수를 계산하는 함수
    return pow(a, p - 2, p)

def comb(n, k, mod):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # n!을 계산
    numerator = 1
    for i in range(n, n - k, -1):
        numerator = (numerator * i) % mod
    
    # k!을 계산
    denominator = 1
    for i in range(1, k + 1):
        denominator = (denominator * i) % mod
    
    # 조합 계산: C(n, k) = n! / (k! * (n-k)!)
    return (numerator * mod_inv(denominator, mod)) % mod

print(comb(N, K, MOD))
