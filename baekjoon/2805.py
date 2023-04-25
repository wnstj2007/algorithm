import sys
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
ans = 0
lo = 0
hi = max(tree)
while lo <= hi:
    mid = (lo+hi)//2
    s = 0
    for i in tree:
        if i > mid:
            s += (i-mid)
    if s >= m:
        lo = mid+1
        ans = max(ans, mid)
    else:
        hi = mid-1
print(ans)