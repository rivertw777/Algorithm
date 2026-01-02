def backtracking(start):
    if len(array) == m:
        print(" ".join(map(str, array)))
        return

    for i in range(start, n):
        array.append(num[i])
        backtracking(i) 
        array.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
array = []

backtracking(0)