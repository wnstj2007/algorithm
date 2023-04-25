input()
angle = {}
ans = 1
n = list(map(int, input().split()))
for i in n:
    angle[i%360] = 1
m = list(map(int, input().split()))
for i in m:
    angle[i%360] = 2
for i in n:
    if angle[i%360]==1:
        ans=0
for i, j in n, m:
    if i-j != tmp:
        ans=0
    tmp = i-j
if ans:
    print('possible')
else:
    print('impossible')