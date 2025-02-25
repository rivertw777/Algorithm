def solution(sticker):
    
    if len(sticker) == 1:
        return sticker[0]
    
    if len(sticker) == 2:
        return max(sticker[0], sticker[1])
    
    # 첫 번째 포함, 마지막 미포함
    new = sticker[:-1]
    dp = [0] * len(new)
    dp[0] = new[0]
    dp[1] = max(new[0], new[1])
    
    for i in range(2, len(new)):
        dp[i] = max(dp[i-1], dp[i-2] + new[i])
    
    case1 = dp[-1]
    
    # 첫 번째 미포함, 마지막 포함
    new = sticker[1:]
    dp = [0] * len(new)
    dp[0] = new[0]
    dp[1] = max(new[0], new[1])
    
    for i in range(2, len(new)):
        dp[i] = max(dp[i-1], dp[i-2] + new[i])
    
    case2 = dp[-1]    
    
    return max(case1, case2)