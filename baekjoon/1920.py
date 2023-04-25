import sys
def search(a, n):
    lo = 0
    hi = len(a)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if a[mid] < n:
            lo = mid+1
        elif a[mid] == n:
            return 1
        else:
            hi = mid-1
    return 0
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
for i in b:
    print(search(a, i))