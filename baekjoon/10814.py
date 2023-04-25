n = int(input())
member = []
for i in range(n):
    member.append(input().split())
ans = sorted(member, key=lambda x: int(x[0]))
for i in ans:
    print(i[0], i[1])