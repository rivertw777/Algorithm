def backtracking():
    if len(array) == m:
        result.add(tuple(array))
        return

    for i in num:
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