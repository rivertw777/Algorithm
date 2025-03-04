def solution(A,B):
    answer = 0

    A.sort()
    B = sorted(B, reverse = True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer