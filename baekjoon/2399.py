n = int(input())
x = sorted(list(map(int, input().split())))
sum = 0
for i in range(len(x)):
    sum += x[i]