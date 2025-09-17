def ccw(x1, y1, x2, y2, x3, y3):
    cal = ((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((y1 * x2) + (y2 * x3) + (y3 * x1))
    if cal > 0:
        return 1
    elif cal == 0:
        return 0
    return -1

# 입력 받기
coords = list(map(int, input().split()))
x1, y1, x2, y2, x3, y3, x4, y4 = coords

# CCW 계산
a = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
b = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

# 결과 출력
if a < 0 and b < 0:
    print(1)
else:
    print(0)