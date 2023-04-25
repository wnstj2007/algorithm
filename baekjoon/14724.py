n = int(input())
people = {}
every = []
club = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
for i in club:
    people[i] = list(map(int,input().split()))
    every.extend(people[i])
ans = max(every)
for i in club:
    if ans in people[i]:
        print(i)