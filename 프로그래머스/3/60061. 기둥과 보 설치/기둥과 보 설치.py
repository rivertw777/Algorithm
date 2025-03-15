def possible(answer):
    for x, y, a in answer:
        if a == 0: # 기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
            
        else: # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False    
    
    return True

def solution(n, build):
    answer = []
    for x, y, a, b in build:
        if b == 0: # 삭제
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
                
        else: # 설치
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])
             
    return sorted(answer)