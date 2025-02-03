answer = 0

def dfs(index, total, numbers, target):
    global answer 

    if index == len(numbers) and total == target:        
        answer += 1
        return
    if index == len(numbers):
        return
    
    dfs(index+1, total + numbers[index], numbers, target)
    dfs(index+1, total - numbers[index], numbers, target)

def solution(numbers, target):    
    dfs(0, 0, numbers, target)
    return answer