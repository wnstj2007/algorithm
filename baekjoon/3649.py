import sys
def search(li, n, i):
    lo = i+1
    hi = len(li)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if li[mid] < n:
            lo = mid+1
        elif li[mid] == n:
            return 1
        else:
            hi = mid-1
    return -1
while True:
    try:
        x = int(sys.stdin.readline())*(10**7)
    except:
        break
    n = int(sys.stdin.readline())
    lego = []
    ans = 0
    for i in range(n):
        lego.append(int(sys.stdin.readline()))
    lego.sort()
    for i in range(len(lego)):
        if lego[i] > x//2:
            break
        if search(lego, x-lego[i],i) == 1:
            ans = (lego[i], x-lego[i])
            #print('yes',i,x-i)
            #ans = 1
            break
    if ans == 0:
        print('danger')
    else:
        print('yes {} {}'.format(ans[0], ans[1]))