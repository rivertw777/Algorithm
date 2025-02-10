import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    # 최대 힙을 만들기 위해 작업량을 음수로 변환
    max_heap = [-work for work in works]
    heapq.heapify(max_heap)
    
    for _ in range(n):
        # 가장 큰 작업량을 꺼내서 1 줄이고 다시 힙에 넣음
        max_work = heapq.heappop(max_heap)
        heapq.heappush(max_heap, max_work + 1)
    
    # 남은 작업량을 제곱하여 합산
    return sum(work**2 for work in max_heap)