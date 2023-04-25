import sys
n, m = map(int, sys.stdin.readline().split())
name = {}
ans = []
for i in range(n):
    t = sys.stdin.readline()
    name[t] = 1
for i in range(m):
    t = sys.stdin.readline()
    try:
        name[t] -= 1
    except:
        pass
for i in name:
    if name[i] == 0:
        i = i.replace('\n', '')
        ans.append(i)
ans.sort()
print(len(ans))
print('\n'.join(ans))