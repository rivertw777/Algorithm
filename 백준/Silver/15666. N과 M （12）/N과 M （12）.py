def backtracking(start):
    if len(array) == m:
        print(*array)
        return
    
    prev = -1  # 이전에 사용한 숫자 추적
    for i in range(start, n):
        # 같은 depth에서 같은 숫자를 중복 사용하지 않음
        if num[i] == prev:
            continue
            
        array.append(num[i])
        backtracking(i)  # 같은 원소 재사용 가능하도록 i부터 시작
        array.pop()
        prev = num[i]

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
array = []
backtracking(0)