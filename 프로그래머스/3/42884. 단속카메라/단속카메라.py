def solution(routes):
    routes.sort(key=lambda x:x[1])
    answer = 1
    point = routes[0][1]
    
    for r in routes:
        if r[0] > point:
            answer+=1
            point = r[1]
        
    return answer