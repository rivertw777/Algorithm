def max_sliding_window(arr):
    max_sum = float('-inf')
    current_sum = 0
        
    start = 0
        
    for end in range(len(arr)):
        current_sum += arr[end]
            
        while start <= end and current_sum < 0:
            current_sum -= arr[start]
            start += 1
            
        max_sum = max(max_sum, current_sum)
        
    return max_sum

def solution(seq):
    p1 = []
    p2 = []
    
    for i in range(len(seq)):
        if i % 2 == 1:
            p1.append(-1)
            p2.append(1)
        else:
            p1.append(1)
            p2.append(-1)
    
    r1 = [a * b for a, b in zip(seq, p1)]
    r2 = [a * b for a, b in zip(seq, p2)]
        
    max1 = max_sliding_window(r1)
    max2 = max_sliding_window(r2)
    
    return max(max1, max2)