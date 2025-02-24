def solution(genres, plays):
    n = len(plays)
    dct = {}
    
    for i in range(n):
        if genres[i] not in dct:
            dct[genres[i]] = plays[i]
        else:
            dct[genres[i]] += plays[i]
        
    sort_g = sorted(dct.items(), key = lambda x:-x[1])
    print(sort_g)
    
    answer = []
    for i in sort_g:
        g = i[0]
        
        temp = []
        for j in range(n):
            if genres[j] == g:
                # 플레이 횟수, 인덱스
                temp.append([plays[j], j])
        
        # 플레이 횟수 많은 순, 인덱스 빠른 순
        temp.sort(key = lambda x: (-x[0], x[1]))
        
        if len(temp) > 0:  # 1개 
            answer.append(temp[0][1])
        if len(temp) > 1: # 2개
            answer.append(temp[1][1])
            
    return answer