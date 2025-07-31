# 다익스트라 
# a가 b에 의존함 => b에서 a로 갈 수 있다 

from heapq import *
import sys
input = sys.stdin.readline
t = int(input()) # 테스트 케이스 수
for _ in range(t):
    n, d, c = map(int, input().split()) # 컴퓨터 수, 의존성 개수, 해킹당한 컴퓨터 번호(시작점)
    graph = [[] for _ in range(n+1)] # 그래프 초기화
    for _ in range(d): 
        a, b, s = map(int, input().split()) # 컴퓨터a, 컴퓨터b, 감염되는데 걸리는 시간
        graph[b].append([a, s]) # 의존하는 쪽으로 갈수있으니 b에 추가
    time = [1e9] * (n + 1) # 시간을 최대값으로 초기화
    heap = [] # 힙
    time[c] = 0 # 시작점은 0으로 초기화
    heappush(heap, [0, c]) # 거리(0), 시작점을 힙에 추가

    while heap: # 힙이 빌때까지 반복
        cur_time, cur_node = heappop(heap) # 현재 소요된 시간, 노드
        if time[cur_node] < cur_time: # 만약 현재 소요된 시간이 더 크다면 이미 최솟값임으로 변경할 필요 없음
            continue
        for next_node, next_time in graph[cur_node]: # 현재 노드에서 갈수있는곳 탐색
            if time[next_node] > cur_time + next_time: # 기존 소요시간보다 현재+다음 시간이 더 적다면
                time[next_node] = cur_time + next_time # 값 갱신
                heappush(heap, [cur_time + next_time, next_node]) # 탐색 위해 힙에 추가
    
    cnt = 0 # 감염된 컴퓨터 개수
    result = 0 # 마지막 컴퓨터 감염되는데 걸리는 시간
    for i in time:
        if i != 1e9: # 초기화된 값이 아니라면
            cnt += 1 # 컴퓨터 개수 증가
            result = max(result, i) # 소요시간 중 최대값을 찾음
    
    print(cnt, result)