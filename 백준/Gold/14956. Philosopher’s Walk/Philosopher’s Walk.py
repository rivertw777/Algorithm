import sys

# 재귀 깊이 제한을 늘려줍니다. (M 값이 클 경우 필요)
sys.setrecursionlimit(10**6) 

def hilbert(N: int, M: int) -> tuple[int, int]:
    """
    힐베르트 곡선의 N x N 그리드에서 M 순번에 해당하는 (x, y) 좌표를 찾습니다.
    (x, y) 좌표는 1부터 시작합니다. M은 0부터 시작하는 순번입니다.
    """
    
    # 1. 기저 사례 (Base Case): N=2 (2x2 그리드)
    if N == 2:
        # M은 0, 1, 2, 3 중 하나입니다.
        if M == 0:
            return 1, 1  # 1사분면 (좌하단)
        elif M == 1:
            return 1, 2  # 2사분면 (좌상단)
        elif M == 2:
            return 2, 2  # 3사분면 (우상단)
        elif M == 3:
            return 2, 1  # 4사분면 (우하단)
        # M의 값이 0~3을 벗어나는 경우는 발생하지 않아야 함

    # 2. 재귀 단계 (Recursive Step)
    half = N // 2
    
    # 현재 순번 M이 어느 4분면에 속하는지 계산합니다.
    # 각 4분면의 크기는 half * half 입니다.
    quadrant_size = half * half
    quadrant = M // quadrant_size
    
    # 다음 재귀 호출에 사용할, 해당 4분면 내의 상대적 순번
    relative_M = M % quadrant_size
    
    # 다음 재귀 호출 결과 (작은 그리드 내의 상대 좌표)
    rel_x, rel_y = hilbert(half, relative_M)
    
    # C++ 코드의 힐베르트 곡선 회전 및 이동 규칙을 Python으로 변환
    
    # 좌하단 (quadrant = 0): W0 변환 (좌표 교환 및 반전)
    if quadrant == 0:
        # (x, y) -> (y, x) 변환
        return rel_y, rel_x

    # 좌상단 (quadrant = 1): W1 변환 (Y축으로 half만큼 이동)
    elif quadrant == 1:
        # (x, y) -> (x, y + half) 변환
        return rel_x, rel_y + half

    # 우상단 (quadrant = 2): W2 변환 (X, Y축으로 half만큼 이동)
    elif quadrant == 2:
        # (x, y) -> (x + half, y + half) 변환
        return rel_x + half, rel_y + half

    # 우하단 (quadrant = 3): W3 변환 (복잡한 회전 후 이동)
    elif quadrant == 3:
        # C++ 코드의 논리: { 2 * half - p.second + 1, half - p.first + 1 }
        # p.first = rel_x, p.second = rel_y
        
        # X 좌표: half + (half - rel_y + 1) = N - rel_y + 1
        # Y 좌표: half + (half - rel_x + 1) = N - rel_x + 1 
        
        # C++ 코드와 동일하게 변환 (복잡한 회전 논리)
        # 새로운 x = 2*half - rel_y + 1
        # 새로운 y = half - rel_x + 1
        
        # 최종 이동 (half만큼 추가 이동)
        new_x = half + (half - rel_y + 1)
        new_y = half - rel_x + 1
        
        # C++ 코드의 리턴 구조와 동일하게 맞추면:
        # pair<int, int> temp = { 2 * half - p.second + 1, half - p.first + 1 }; 
        # C++ 코드를 그대로 반영한 최종 좌표 (여기서 다시 half를 더해야 하나? C++ 코드가 이미 최종 좌표를 계산하는 것처럼 보임)
        
        # C++ 코드를 분석하면, W3 변환은 (x, y) -> (N - y + 1, N - x + 1) 변환 후 좌상단으로 옮겨진 형태의 복잡한 변환입니다.
        
        # C++ 코드를 그대로 반영한 변환:
        final_x = 2 * half - rel_y + 1
        final_y = half - rel_x + 1
        
        # 하지만 힐베르트 곡선의 W3 변환은 일반적으로 다음과 같습니다:
        # (x, y) -> (2*half - y + 1 + half, half - x + 1) 
        # C++ 코드를 따르면, W3 영역은 4분면 중 우하단이 아니라 좌하단에서 시작하는 좌표 시스템을 가정하는 듯합니다.
        
        # C++ 코드의 구현을 그대로 따라갑니다. (최종 좌표를 만들기 위한 특수한 변환)
        final_x = 2 * half - rel_y + 1
        final_y = half - rel_x + 1
        
        return final_x, final_y

def main():
    try:
        # N: 그리드 크기 (2^k 형태), M: 순번 (1부터 시작)
        # N은 2^k 형태의 정수, M은 1부터 시작하는 정수입니다.
        N, M = map(int, sys.stdin.readline().split())
    except:
        # 입력이 없거나 형식이 잘못된 경우
        return

    # M은 1부터 시작하는 순번이므로, 0부터 시작하는 인덱스로 변환하여 함수에 전달합니다.
    # C++ 코드의 main 함수에서 M - 1을 하는 것과 동일합니다.
    result_x, result_y = hilbert(N, M - 1)

    print(f"{result_x} {result_y}")

if __name__ == "__main__":
    main()