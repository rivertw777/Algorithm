def solution(n, s):
    a = int(s/n)    
    
    if a == 0:
        return [-1]
    
    b = s % n
    
    answer = []    
    for i in range(n-b):
        answer.append(a)
    for i in range(b):
        answer.append(a+1)

    return answer