import sys
import heapq
n, k = map(int, sys.stdin.readline().split())
bag = []
jewel = []
heap = []
ans = 0
for i in range(n):
    jewel.append(tuple(map(int, sys.stdin.readline().split())))
jewel.sort()
for i in range(k):
    bag.append(int(sys.stdin.readline()))
bag.sort()
t = 0
for i in bag:
    for j in range(t,len(jewel)):
        if jewel[j][0] > i:
            break
        t = j+1
        heapq.heappush(heap, -jewel[j][1])
    if heap:
        ans -= heapq.heappop(heap)
print(ans)