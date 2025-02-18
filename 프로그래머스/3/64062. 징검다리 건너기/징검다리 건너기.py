from collections import deque

def solution(stones, k):
    n = len(stones)
    q = deque()
    answer = float('inf')

    for i in range(n):
        while q and q[0][1] <= i - k:
            q.popleft()
        
        while q and q[-1][0] < stones[i]:
            q.pop()
        
        q.append((stones[i], i))
        
        if i >= k - 1:
            answer = min(answer, q[0][0])
    
    return answer