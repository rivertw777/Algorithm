import sys
input = sys.stdin.readline
def ccw(x1, y1, x2, y2, x3, y3):
    return  x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a = ccw(x1, y1, x2, y2, x3, y3)  # 선분1 기준으로 점3의 방향
b = ccw(x1, y1, x2, y2, x4, y4)  # 선분1 기준으로 점4의 방향
c = ccw(x3, y3, x4, y4, x1, y1)  # 선분2 기준으로 점1의 방향  
d = ccw(x3, y3, x4, y4, x2, y2)  # 선분2 기준으로 점2의 방향

if a * b == 0 and c * d == 0:
    if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4):
        print(1)
    else:
        print(0)
else:
    if a * b <= 0 and c * d <= 0:
        print(1)
    else:
        print(0)