def solution(n, times):
    start, end =  1, times[-1] * n

    while start < end:
        mid = (start + end) // 2
        
        total = 0
        for time in times:
            total += mid // time
        
        if total >= n:
            end = mid
        else:
            start = mid + 1
    
    return end