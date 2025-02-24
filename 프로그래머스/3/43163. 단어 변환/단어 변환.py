answer = 0

def dfs(begin, target, words, count):
    global answer
    
    if begin == target:
        answer = count
        return 
        
    for w in words:
        
        dif = 0
        for i in range(len(w)):
            if begin[i] != w[i]:
                dif += 1
        
        if dif == 1:
            new_words = words[:]
            new_words.remove(w)
            dfs(w, target, new_words, count+1)
    
    
def solution(begin, target, words):
    global answer
    dfs(begin, target, words, 0)
    return answer
