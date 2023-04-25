n = int(input())
sum = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in tmp:
        sum += j
print(sum)