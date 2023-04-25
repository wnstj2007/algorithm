a, b, v = map(int, input().split())
lo = 0
hi = v//(a-b) if v%(a-b) == 0 else (v//(a-b))+1
ans = hi
while lo <= hi:
    mid = (lo+hi)//2
    t = (a-b)*(mid-1)+a
    if t >= v:
        hi = mid-1
        ans = min(ans, mid)
    else:
        lo = mid+1
print(ans)