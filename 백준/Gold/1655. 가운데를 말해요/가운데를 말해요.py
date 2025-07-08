import sys
import heapq

minHeap = []
maxHeap = []
answer = []

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    
    if len(minHeap) == len(maxHeap):
        heapq.heappush(minHeap, (-num, num))
    else:
        heapq.heappush(maxHeap, (num, num))
        
    if maxHeap and minHeap[0][1] > maxHeap[0][0]:
        min = heapq.heappop(maxHeap)[0]
        max = heapq.heappop(minHeap)[1]
        heapq.heappush(minHeap, (-min, min))
        heapq.heappush(maxHeap, (max, max))
        
    answer.append(minHeap[0][1])
    
for i in answer:
    print(i)