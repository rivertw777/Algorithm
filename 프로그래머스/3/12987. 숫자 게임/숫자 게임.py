def solution(a, b):
    answer = 0
    a.sort()
    b.sort()
    
    index = 0
    for i in range(len(a)):
        if b[i] > a[index]:
            answer += 1
            index += 1

    return answer