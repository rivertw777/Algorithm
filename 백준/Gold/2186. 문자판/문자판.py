import sys

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())

matrix = [input().rstrip() for _ in range(N)]

st = input().rstrip()

# dp[y][x][idx] : (y, x)에 idx번 째로 방문했을 때 만들어지는 경우의 수 memoization
dp_matrix = [[[-1 for _ in range(len(st))] for _ in range(M)] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
count = 0


def dfs(idx, y, x):
    # memoization 되어있는 경우 바로 결과 반환
    if dp_matrix[y][x][idx] != -1:
        return dp_matrix[y][x][idx]

    # 글자가 완성되는 경우 카운트 추가
    if idx == len(st) - 1:
        return 1

    # 새로운 memoization을 위한 카운트 이를 기점으로 앞으로의 경우의 수 카운트
    cnt = 0
    # 상하좌우 최대 k칸
    for k in range(1, K + 1):
        for d in range(4):
            ny = y + k * dy[d]
            nx = x + k * dx[d]
			# 다음 문자가 일치하는 경우만 재귀
            if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == st[idx + 1]:
                cnt += dfs(idx + 1, ny, nx)

    # 경우의 수 memoization 업데이트
    dp_matrix[y][x][idx] = cnt

    return cnt


for r in range(N):
    for c in range(M):
        if matrix[r][c] == st[0]:
            count += dfs(0, r, c)

print(count)