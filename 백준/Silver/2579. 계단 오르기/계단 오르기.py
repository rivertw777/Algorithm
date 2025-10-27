n = int(input())

step = []
for _ in range(n):
    step.append(int(input()))

if n == 1:
    print(step[0])
elif n == 2:
    print(step[0] + step[1])
else:
    # DP[i][0]: 1칸 연속으로 i번째 계단에 도착한 최대 점수
    # DP[i][1]: 2칸 점프로 i번째 계단에 도착한 최대 점수
    # (배열 크기는 n+1로, step 배열은 0부터 n-1까지 사용)
    dp = [[0] * 2 for _ in range(n)] 

    # 초기값 설정 (0번째 계단은 0점)
    # 1번째 계단 (step[0] = 10)
    dp[0][0] = step[0] # 1칸 연속
    dp[0][1] = step[0] # 2칸 점프 (의미 없음, 초기값은 동일)

    # 2번째 계단 (step[1] = 20)
    dp[1][0] = dp[0][1] + step[1] # 10 + 20 = 30 (1칸 연속)
    dp[1][1] = step[1]           # 20 (2칸 점프)
    
    # DP 루프 시작 (3번째 계단부터, 인덱스 2부터)
    for i in range(2, n):
        current_score = step[i]

        # 1. 1칸 연속으로 i에 도착 (i-1에서 옴): 
        #    i-1에는 2칸 점프로 도착한 경우만 허용 (연속 3칸 방지)
        dp[i][0] = dp[i-1][1] + current_score

        # 2. 2칸 점프로 i에 도착 (i-2에서 옴): 
        #    i-2에 1칸 연속으로 왔든, 2칸 점프로 왔든 상관 없음 (최댓값 선택)
        dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + current_score

    # 최종 결과: 마지막 계단에 1칸 연속으로 도달했거나, 2칸 점프로 도달한 경우 중 최댓값
    final_answer = max(dp[n-1][0], dp[n-1][1])
    print(final_answer)