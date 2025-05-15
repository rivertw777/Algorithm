def solution(sticker):
    answer = 0
    n = len(sticker)

    if n == 1:
        return sticker[0]

    if n == 2:
        return max(sticker[0], sticker[1])

    # 첫 번째 포함, 마지막 미포함
    new = sticker[:-1]
    dp1 = [0] * (n - 1)
    dp1[0] = new[0]
    dp1[1] = max(new[0], new[1])
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i-2] + new[i], dp1[i-1]) 

    # 첫 번째 미포함, 마지막 포함
    new = sticker[1:]
    dp2 = [0] * n 
    dp2[0] = new[0]
    dp2[1] = max(new[0], new[1])
    for i in range(2, n - 1):
        dp2[i] = max(dp2[i-2] + new[i], dp2[i-1])

    return max( max(dp1), max(dp2) )