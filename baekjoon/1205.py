n, score, p = map(int, input().split())
rank = []
if n != 0:
    rank = list(map(int, input().split()))
if n < p:
    rank.append(score)
    print(sorted(rank, reverse=True).index(score)+1)
elif score > rank[-1]:
    rank[-1] = score
    rank.sort(reverse=True)
    print(rank.index(score)+1)
else:
    print(-1)