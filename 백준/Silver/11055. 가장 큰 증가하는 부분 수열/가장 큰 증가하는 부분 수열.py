n = int(input())
# 입력 값이 없을 경우를 대비하여 예외 처리
if n == 0:
    print(0)
    # return을 사용하여 함수/스크립트를 종료하는 것이 좋습니다.
    # return
    
# n > 0 인 경우에만 arr을 입력 받습니다.
if n > 0:
    arr = list(map(int, input().split()))

    # dp[i]: arr[i]를 '반드시 포함'하는 LIS의 최대 합
    dp = [0] * n

    # 정방향으로 배열을 순회하며 DP 수행
    for i in range(n):
        # 1. 초기값 설정: arr[i] 혼자서 이루는 수열의 합
        dp[i] = arr[i]
        
        # 2. i 이전의 모든 원소 j를 탐색
        for j in range(i):
            # 3. 오름차순 조건 확인: arr[j]가 arr[i]보다 작다면 연결 가능
            if arr[j] < arr[i]:
                # dp[i] = arr[i] + (arr[j]를 포함하는 LIS의 최대 합) 중 최댓값 갱신
                # 즉, arr[i]를 끝으로 하는 수열의 합 = 현재 arr[i] 값 + 이전의 최대 합
                dp[i] = max(dp[i], arr[i] + dp[j])
                
    # dp 배열의 모든 값 중에서 최대를 찾으면 그것이 전체 LIS Sum의 최댓값
    print(max(dp))