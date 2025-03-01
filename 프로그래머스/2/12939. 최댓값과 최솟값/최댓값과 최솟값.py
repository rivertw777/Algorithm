def solution(s):
    a = s.split(" ")
    
    answer = []
    for i in a:
        answer.append(int(i))
        
    return str(min(answer)) + " " + str(max(answer))