#백준 9203 호텔 예약
#datetime
import datetime

def find(log, request):
    tmplog = []
    for i in log:
        for j in log[i]:
            if j <= request:
                tmplog.append([j, i])
    if len(tmplog) == 0:
        print('Internal')
    else:
        print(max(tmplog)[1])

n, m = map(int, input().split())
name = input().split()
log = {}
for i in name:
    log[i] = []

for i in range(m):
    li = input().split()
    time = datetime.datetime.strptime(li[1][:19], '%Y-%m-%dT%H:%M:%S')
    time -= datetime.timedelta(hours=int(li[1][19:22]), minutes=int(li[1][23:]))
    log[li[0]].append(time)

find_time = input()
request = datetime.datetime.strptime(find_time[:19], '%Y-%m-%dT%H:%M:%S')
request -= datetime.timedelta(hours=int(find_time[19:22]), minutes=int(find_time[23:]))
find(log,request)