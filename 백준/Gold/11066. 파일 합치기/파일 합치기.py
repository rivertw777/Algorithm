import sys
input = sys.stdin.readline

def solve_file_merge():
    T = int(input())
    
    for _ in range(T):
        K = int(input())
        files = list(map(int, input().split()))
        
        # 누적 합 배열 생성
        prefix_sum = [0] * (K + 1)
        for i in range(K):
            prefix_sum[i + 1] = prefix_sum[i] + files[i]
        
        # dp[i][j] = i번째부터 j번째까지 파일을 합치는 최소 비용
        # opt[i][j] = dp[i][j]를 달성하는 최적 분할점
        dp = [[0] * K for _ in range(K)]
        opt = [[0] * K for _ in range(K)]
        
        # 기저 조건: 길이 1인 구간은 비용 0
        for i in range(K):
            opt[i][i] = i
        
        # 구간 길이별로 계산 (길이 2부터 K까지)
        for length in range(2, K + 1):
            for i in range(K - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                
                # 구간 합을 미리 계산
                range_sum = prefix_sum[j + 1] - prefix_sum[i]
                
                # Knuth-Yao 최적화: 탐색 범위를 줄임
                start = opt[i][j - 1] if j > i else i
                end = opt[i + 1][j] if i + 1 <= j else j - 1
                
                for k in range(start, min(end + 1, j)):
                    cost = dp[i][k] + dp[k + 1][j] + range_sum
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        opt[i][j] = k
        
        print(dp[0][K - 1])

# 실행
solve_file_merge()