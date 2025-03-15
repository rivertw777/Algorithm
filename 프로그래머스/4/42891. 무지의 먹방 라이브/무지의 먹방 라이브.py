import heapq as hq

def solution(ft, k):
    if sum(ft) <= k:
        return - 1
    
    q = []
    for i in range(len(ft)):
        hq.heappush(q, (ft[i], i + 1))
                
    spend = 0 # 먹기 위해 사용한 시간
    just_spend = 0 # 직전에 다 먹은 음식 시간
    rest = len(ft) # 남은 음식 개수
    
    while spend + ((q[0][0] - just_spend) * rest) <= k: # 현재 시간에서 추가로 더 먹어도 k보다 작을 때
        
        now = hq.heappop(q)[0] # 음식 먹을 수 있는 시간
        
        spend += (now - just_spend) * rest # 현재 시간에 음식 추가로 먹은 시간 추가
        
        rest -= 1 # 음식 개수 제거
        
        just_spend = now 
        
    result = sorted(q, key = lambda x:x[1])
    return result[(k - spend) % rest][1]