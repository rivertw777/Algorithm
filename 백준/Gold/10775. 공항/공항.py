import sys


# 부모 테이블 찾기
def find(x):
    # 비행기 번호와 부모 테이블 번호가 같으면 비행기 번호 리턴
    if parent[x] == x:
        return x
    # 재귀적으로 부모 테이블을 찾는다.
    # 부모 테이블 리턴
    parent[x] = find(parent[x])
    return parent[x]


# 부모 테이블 바꾸기
def union(a, b):
    a = find(a)
    b = find(b)
    # 부모 테이블을 -1 해준 값으로 바꿔 앞에 부모 테이블과 연결한다.
    parent[b] = a


G = int(sys.stdin.readline())
p = int(sys.stdin.readline())
g = [int(sys.stdin.readline()) for x in range(p)]

# 부모 테이블 초기화
parent = [i for i in range(G + 1)]
# 도킹 횟수
cnt = 0

for i in g:
    # 현재 도킹하려는 게이트
    docking = find(i)

    # 도킹할 곳이 없으므로 멈춘다.
    if docking == 0:
        break

    # 도킹 횟수 카운트
    cnt += 1
    # 현재 번호 비행기가 도킹을 했으므로 -1을 해준다.
    union(docking - 1, docking)

print(cnt)