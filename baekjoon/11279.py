import heapq
import sys
n = int(sys.stdin.readline())
heap = []
for i in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-m, m))