def backtracking():
    if len(array) == m:
        copy = sorted(array)
        result.add(tuple(copy))
        return

    for i in num:
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
array = []
result = set()

backtracking()

result = list(result)
result.sort()
for i in result:
    print(" ".join(map(str, i)))