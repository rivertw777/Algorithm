def solution(n, stations, w):
    answer = 0
    cur = 1
    index = 0 
    while cur <= n:        
        if index < len(stations) and cur >= stations[index] - w:
            cur = stations[index] + w + 1
            index += 1
        else:
            cur += 2 * w + 1 
            answer += 1
    
    return answer