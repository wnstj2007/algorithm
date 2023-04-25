n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]
schedule.sort(key=lambda x: (x[1], x[0]))

time = 0
count = 0
for i in schedule:
    if time <= i[0]:
        time = i[1]
        count += 1

print(count)