def solution(n, stages):
    ans = []
    l = len(stages)
    
    for i in range(1, n+1):
        cnt = stages.count(i)
        
        if l == 0:
            fail = 0
        else:
            fail = cnt / l
                
        ans.append((i, fail))
        l -= cnt
                
    ans = sorted(ans, key=lambda x:x[1], reverse=True)
    
    return [i[0] for i in ans]