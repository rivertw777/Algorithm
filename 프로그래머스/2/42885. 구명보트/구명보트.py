def solution(p, limit):
    p.sort()
    
    cnt = 0
    a = 0
    b = len(p) -1 
    while a <= b:        
        if p[a] + p[b] <= limit:
            cnt += 1
            a += 1
            b -= 1
        else:
            cnt += 1
            b -= 1
                      
    return cnt