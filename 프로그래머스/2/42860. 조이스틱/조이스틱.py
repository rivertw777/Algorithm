def solution(name):
    answer = 0
    move = len(name) - 1
    for i, char in enumerate(name):
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1
        move = min([move, i * 2 + len(name) - next, i + (len(name) - next) * 2])
    answer += move
    return answer