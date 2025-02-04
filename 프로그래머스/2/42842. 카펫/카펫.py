def solution(b, r):
    sum = b+r
    
    for x in range(1, sum+1):
        if sum % x != 0:
            continue
        
        y = sum//x
        
        if (x-2) * (y-2) == r:
            return sorted([x,y], reverse=True)