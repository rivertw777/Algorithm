def solution(elements):
    n = len(elements)
    res = set()

    for i in range(n):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+n):
            ssum += elements[j%n]
            res.add(ssum)
    return len(res)