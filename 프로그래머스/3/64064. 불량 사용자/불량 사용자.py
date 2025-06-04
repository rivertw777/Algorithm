def is_matching(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    
    for i in range(len(user_id)):
        if banned_id[i] != '*' and banned_id[i] != user_id[i]:
            return False
        
    return True

def dfs(user_id, banned_id, index, temp, result):
    # 모든 banned_id를 처리했으면 결과에 추가
    if index == len(banned_id):
        result.add(tuple(sorted(temp)))
        return
    
    # 현재 banned_id와 매칭되는 user_id들을 찾아서 시도
    for user in user_id:
        if user not in temp and is_matching(user, banned_id[index]):
            temp.append(user)
            dfs(user_id, banned_id, index + 1, temp, result)
            temp.pop()  # 백트래킹

def solution(user_id, banned_id):
    result = set()
    temp = []
    dfs(user_id, banned_id, 0, temp, result)
    return len(result)
