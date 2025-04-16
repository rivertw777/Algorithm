def solution(genres, plays):    
    n = len(genres)
    most = {}
    for i in range(n):    
        if genres[i] in most:
            most[genres[i]] += plays[i]
        else:
            most[genres[i]] = plays[i]
        
    # 속한 노래가 많이 재생된 장르
    most = sorted(most.items(), key = lambda x:-x[1])

    answer = []
    for i in most:
        g = i[0]         
        temp = []
        for j in range(n):
            if g == genres[j]:
                temp.append([j, plays[j]])

        temp.sort(key=lambda x:(-x[1], x[0]))

        if len(temp) >= 2:
            answer.append(temp[0][0])
            answer.append(temp[1][0])
        else:
            answer.append(temp[0][0])
    
    return answer 