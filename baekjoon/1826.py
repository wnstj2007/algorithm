import heapq
import sys
n = int(sys.stdin.readline())
dist = []
heap = []
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    dist.append((a,b))
city, stock = map(int, sys.stdin.readline().split())
dist.sort()
ans = 0
while city > stock:
    used = []
    for i in dist:
        if i[0] <= stock:
            heapq.heappush(heap, -i[1])
            used.append(i)
    for i in used:
        dist.remove(i)
    if not heap:
        break
    stock -= heapq.heappop(heap)
    ans += 1

if city > stock:
    print(-1)
else:
    print(ans)