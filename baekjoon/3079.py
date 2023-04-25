import sys
def search(li, m):
    lo = 0
    hi = max(li)*m
    ans = hi
    while lo <= hi:
        mid = (lo+hi)//2
        s = 0
        for i in li:
            s += mid//i
        if s < m:
            lo = mid+1
        else:
            ans = min(ans, mid)
            hi = mid-1
    return ans

n, m = map(int, sys.stdin.readline().split())
t = []
for i in range(n):
    t.append(int(sys.stdin.readline()))
print(search(t, m))