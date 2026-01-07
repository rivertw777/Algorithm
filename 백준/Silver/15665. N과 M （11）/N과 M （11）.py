def backtracking():
    if len(array) == m:
        if tuple(array) in result:
            return 
            
        print(*array)
        result.add(tuple(array[:]))
        return

    for i in range(n):
        array.append(num[i])
        backtracking()  
        array.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = set()

array = []
backtracking()