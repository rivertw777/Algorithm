from itertools import permutations

def is_matching(user_id, ban_id):
    """주어진 user_id가 ban_id와 일치하는지 확인."""
    if len(user_id) != len(ban_id):
        return False
    for u_char, b_char in zip(user_id, ban_id):
        if b_char != '*' and u_char != b_char:
            return False
    return True

def solution(user_id, banned_id):
    answer = set()
    banlist = set()

    # 사용자 ID와 금지된 ID 매칭
    for ban_id in banned_id:
        for uid in user_id:
            if is_matching(uid, ban_id):
                banlist.add(uid)

    # 가능한 모든 순열 생성
    for per in permutations(banlist, len(banned_id)):
        if all(is_matching(per[i], banned_id[i]) for i in range(len(per))):
            answer.add(tuple(sorted(per)))  # 정렬하여 중복 방지

    return len(answer)
