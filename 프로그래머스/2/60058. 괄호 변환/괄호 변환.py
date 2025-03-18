def check(u): # 짝도 맞아야 통과
    count = 0
    for i in u:
        if i ==  '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
            
    return True

def solution(p):
    if p == "":
        return p
    
    count = 0
    for i in range(len(p)): # 개수만 맞으면 통과
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            index = i
            break
            
    u = p[:index+1]
    v = p[index+1:]
    print(u, v)
    
    if check(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = list(u[1:-1])     
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer