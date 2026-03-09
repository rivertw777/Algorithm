def backtracking(start, depth):
    # 6개를 모두 고르면 출력하고 종료
    if depth == 6:
        print(*(array))
        return

    # start 인덱스부터 k까지 반복 (조합 생성)
    for i in range(start, k):
        array.append(S[i])
        # 다음 숫자는 현재 숫자(i)의 다음 인덱스부터 탐색
        backtracking(i + 1, depth + 1)
        # 백트래킹: 선택했던 숫자를 빼고 다음 루프로 이동
        array.pop()

while True:
    line = list(map(int, input().split()))
    
    # 0이 입력되면 종료
    if line[0] == 0:
        break
    
    k = int(line[0])
    S = list(map(int, line[1:]))
    
    array = []
    backtracking(0, 0)

    print()