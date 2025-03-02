def solution(gems):
    total = len(set(gems))
    if total == 1:
        return [1,1]
    
    answer = []
    
    temp = {}
    temp[gems[0]] = 1
    start, end = 1,1
    while end <= len(gems):
                        
        if len(temp) < total:  
            if end == len(gems):
                break
            end += 1
            
            if gems[end-1] not in temp:
                temp[gems[end-1]] = 1
            else:
                temp[gems[end-1]] += 1
            
        elif len(temp) == total:
            answer.append((start, end))
            
            if temp[gems[start-1]] == 1:
                del temp[gems[start-1]]
            else:
                temp[gems[start-1]] -= 1
            
            start += 1
            
    answer.sort(key = lambda x: x[1]-x[0])
    return list(answer[0])