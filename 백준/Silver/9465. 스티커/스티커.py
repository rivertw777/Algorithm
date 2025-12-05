t = int(input())

for _ in range(t):
    
    n = int(input())
    st = []
    for i in range(2):
        st.append(list(map(int, input().split())))

    if n == 1:
        print(max(st[0][0], st[1][0]))
    elif n == 2:
        print(max(st[0][0] + st[1][1],  st[1][0] + st[0][1]))
    else:
        dp = [ [0] * n for _ in range(2) ] 
        
        # dp[0]
        dp[0][0] = st[0][0]
        dp[1][0] = st[1][0]

        # dp[1]
        dp[0][1] = dp[1][0] + st[0][1]
        dp[1][1] = dp[0][0] + st[1][1]
        
        # dp[2] ~ dp[n-1]
        for i in range(2, n):
            dp[0][i] = max( dp[1][i-1] + st[0][i], max(dp[0][i-2], dp[1][i-2]) + st[0][i] )
            dp[1][i] = max( dp[0][i-1] + st[1][i], max(dp[0][i-2], dp[1][i-2]) + st[1][i] )    
        
        print(max(  max(dp[0]), max(dp[1]) ))