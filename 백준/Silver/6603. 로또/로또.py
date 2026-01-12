import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
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

# 첫 번째 케이스인지 확인하기 위한 플래그 (빈 줄 출력용)
first_case = True

while True:
    line = sys.stdin.readline().split()
    
    # 0이 입력되면 종료
    if line[0] == '0':
        break
    
    # 첫 번째 수는 k, 나머지는 집합 S
    k = int(line[0])
    S = list(map(int, line[1:]))
    
    # 테스트 케이스 사이에는 빈 줄을 출력 (첫 번째 케이스 제외)
    if not first_case:
        print()
    
    array = []
    backtracking(0, 0)
    
    # 다음 케이스부터는 빈 줄을 출력하도록 설정
    first_case = False