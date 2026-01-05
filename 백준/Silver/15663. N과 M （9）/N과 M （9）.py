def backtracking():
    if len(array) == m:
        print(" ".join(map(str, array)))
        return

    last_used = -1  # 현재 깊이(level)에서 마지막으로 선택한 숫자를 저장
    
    for i in range(n):
        # 1. 이미 사용한 인덱스이거나, 
        # 2. 이번 루프에서 이미 선택했던 숫자와 같다면 건너뜀
        if not visited[i] and num[i] != last_used:
            visited[i] = True
            array.append(num[i])
            last_used = num[i]  # 선택한 숫자를 기록
            
            backtracking()      # 다음 숫자 선택하러 가기
            
            array.pop()
            visited[i] = False

# 입력 받기
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

array = []
visited = [False] * n
backtracking()