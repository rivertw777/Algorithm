
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
def solution(sequence, k):
    answer = []
    temp = sequence[0]
    start,end = 0,0
    while end <= len(sequence):
        if temp < k:
            if end + 1 == len(sequence):
                break
            end += 1
            temp += sequence[end]
        elif temp > k:
            temp -= sequence[start]
            start += 1
        elif temp == k:
            answer.append((start,end))
            temp -= sequence[start]
            start += 1
    answer = sorted(answer,key=lambda x: x[1]-x[0])

    return answer[0]