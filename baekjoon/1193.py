from math import ceil

x = int(input())
n = 1
for i in range(ceil(x**(1/2))+1):
    print(i, i * (i + 1) // 2)
    if x <= i * (i + 1) // 2:
        n = i - 1
        break

x -= n * (n + 1) // 2

print(f'{x}/{n + 1 - (x - 1)}')