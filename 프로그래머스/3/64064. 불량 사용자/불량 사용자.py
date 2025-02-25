from itertools import permutations

def is_matching(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    
    for i in range(len(user_id)):
        if banned_id[i] != '*' and banned_id[i] != user_id[i]:
            return False
        
    return True

def solution(user_id, banned_id): 
    ban_list = set()
    for i in banned_id:
        for j in user_id:
            if is_matching(j, i):
                ban_list.add(j)
    
    answer = set()
    for per in permutations(ban_list, len(banned_id)):
        flag = True  
        for i in range(len(per)):
            if not is_matching(per[i], banned_id[i]):
                flag = False 
                break  
        if flag:
            answer.add(tuple(sorted(per)))

    return len(answer)