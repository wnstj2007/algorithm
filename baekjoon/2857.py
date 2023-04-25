ans = []
for i in range(1,6):
    agent = input()
    if 'FBI' in agent:
        ans.append(i)
if len(ans) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(map(str, ans)))