def backtracking():
    sorted_tuple = tuple(sorted(array))
    if len(array) == m and sorted_tuple not in s:
        print(" ".join(map(str, array)))
        s.add(sorted_tuple)
        return

    for i in range(1, n+1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()

n, m = map(int,input().split())
array = []
s = set()

backtracking()