def solution(gems):    
    total = len(set(gems))
    if total == 1:
        return [1,1]
        
    
    answer = []    
    temp = {}
    temp[gems[0]] = 1  #  딕셔너리에 보석 이름 저장
    start, end = 1,1
    while end <= len(gems):
        if len(temp) < total:  #  조건에 안맞으면 종료 포인트 증가
            if end == len(gems):
                break
            end += 1
            
            if gems[end-1] not in temp: # 현재 종료 지점의 보석이 없을때
                temp[gems[end-1]] = 1
            else:                       # 있을 때
                temp[gems[end-1]] += 1
            
        elif len(temp) == total: # 조건에 맞으면 시작 포인트 증가
            answer.append((start, end))
            
            if temp[gems[start-1]] == 1: # 현재 시작점의 보석이 1개일 때
                del temp[gems[start-1]]
            else:                        # 그 이상일 때 
                temp[gems[start-1]] -= 1 
            
            start += 1  
            
    answer.sort(key = lambda x: x[1] - x[0])
    return list(answer[0])