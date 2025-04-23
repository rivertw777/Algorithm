def solution(routes):
    routes.sort(key=lambda x:x[1])
    
    answer = 1
    index = 0
    cur = routes[0][1]
    while index < len(routes):
        if cur < routes[index][0]:
            cur = routes[index][1]
            answer += 1
        index += 1
        
    return answer