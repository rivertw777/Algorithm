def backtracking():
    if len(array) == m:
        print(*array)
        return

    last_used = -1
    for i in range(n):        
        # 1. 이미 사용한 인덱스이거나, 
        # 2. 이번 루프에서 이미 선택했던 숫자와 같다면 건너뜀
        # 3. 이미 array에 있는 원소보다 크거나 같아야 함
        if not visited[i] and num[i] != last_used and ((array and array[-1] <= num[i]) or (not array)):
            visited[i] = True
            array.append(num[i])
            last_used = num[i]            
            backtracking()  
            array.pop()
            visited[i] = False

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

array = []
visited = [False] * n
backtracking()