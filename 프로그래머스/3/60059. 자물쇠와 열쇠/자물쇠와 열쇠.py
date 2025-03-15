def turn(key):
    n = len(key)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = key[i][j]
    return result

def check(new_lock):
    l = len(new_lock) // 3
    for i in range(l, l * 2):
        for j in range(l, l * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]  # 중앙에 자물쇠 배치

    m = len(key)
    for i in range(1, 2 * n):
        for j in range(1, 2 * n):
            for _ in range(4):
                key = turn(key)  # 회전된 키
                for x in range(m):
                    for y in range(m):
                        new_lock[i + x][j + y] += key[x][y]
                
                if check(new_lock):
                    return True
                
                for x in range(m):
                    for y in range(m):
                        new_lock[i + x][j + y] -= key[x][y]  # 원래 상태로 되돌리기

    return False
