import sys
# 입력 데이터가 많으므로 sys.stdin.readline을 사용합니다.
try:
    # 첫 줄 T, W를 읽습니다.
    T, W = map(int, sys.stdin.readline().split())
except:
    # 입력이 없거나 형식이 잘못된 경우를 대비합니다.
    T, W = 0, 0
    
if T > 0:
    # 각 초에 자두가 떨어지는 나무 번호 (1 또는 2)를 loc 리스트에 저장
    loc = [0] * (T + 1)
    for i in range(1, T + 1):
        loc[i] = int(sys.stdin.readline().strip())
else:
    # T=0이면 자두가 없습니다.
    loc = [0]

# DP[t][w]: t초까지 w번 움직여 잡은 최대 자두 개수
dp = [[0] * (W + 1) for _ in range(T + 1)]

if T > 0:
    # 1. 초기값 설정 (t=1)
    
    # w=0 (0번 이동): 1번 나무 위치
    if loc[1] == 1:
        dp[1][0] = 1
    else:
        dp[1][0] = 0
        
    # w=1 (1번 이동): 2번 나무 위치 (W >= 1일 때만 가능)
    if W >= 1:
        if loc[1] == 2:
            dp[1][1] = 1
        else:
            dp[1][1] = 0
            
    # 2. 전이식 (t=2 부터 T까지)
    for t in range(2, T + 1):
        
        # --- (1) w=0 일 때 (움직이지 않고 1번 나무에 머무름) ---
        # 직전 t-1에서 0번 이동한 경우만 가능
        catch_at_tree_1 = 1 if loc[t] == 1 else 0
        dp[t][0] = dp[t-1][0] + catch_at_tree_1

        # --- (2) w > 0 일 때 ---
        for w in range(1, W + 1):
            
            # 현재 t초에 자두가 있는 나무 번호 (w가 짝수면 1번, 홀수면 2번)
            current_tree = (w % 2) + 1 
            catch_count = 1 if loc[t] == current_tree else 0

            # 1. 가만히 있었을 경우 (Stay): t-1초에 이미 w번 이동
            stay_count = dp[t-1][w]
            
            # 2. 움직였을 경우 (Move): t-1초에 w-1번 이동 후, t초에 1번 이동
            move_count = 0
            if w >= 1:
                move_count = dp[t-1][w-1]
            
            # 두 경우 중 최대값에 현재 잡은 자두 개수를 더함
            dp[t][w] = max(stay_count, move_count) + catch_count
            
    # 3. 최종 결과 출력
    # T초까지 모든 이동 횟수(0 ~ W) 중 최대값을 출력
    print(max(dp[T]))
else:
    print(0)