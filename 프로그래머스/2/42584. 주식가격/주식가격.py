from collections import deque

def solution(prices):
    q = deque(prices)
    
    answer = []
    while q:
        item = q.popleft()
        
        cnt = 0
        for i in q:
            cnt += 1
            if item > i:
                break
        answer.append(cnt)

    return answer