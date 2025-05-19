answer = 1e9

def dfs(begin, target, words, cnt):
    global answer

    if begin == target:
        answer = min(answer, cnt)

    for word in words:
        dif = 0
        for i in range(len(word)):
            if begin[i] != word[i]:
                dif += 1

        if dif == 1:
            new = words[:]
            new.remove(word)
            dfs(word, target, new, cnt+1)
            
def solution(begin, target, words):
    dfs(begin, target, words, 0)
    
    if answer == 1e9:
        return 0
    return answer