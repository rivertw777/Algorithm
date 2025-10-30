import sys

# sys.stdin.readline 사용
def input():
    return sys.stdin.readline().rstrip()

# N, M 입력
n, m = map(int, input().split())

# numbers 입력
# sys.stdin.readline()을 직접 사용 (map과 함께)
numbers = list(map(int, sys.stdin.readline().split())) 

# --- (Prefix Sum 생성 로직은 동일) ---
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i-1] + numbers[i-1]
    
# M개의 질문 처리 시에도 sys.stdin.readline 사용
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    
    # 계산 로직은 O(1)로 동일
    print(dp[end] - dp[start - 1])