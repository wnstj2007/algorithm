def sum(n):
    if n<3:
        return n
    dp = [0, 1, 2, 4] + [0 for i in range(n-3)]
    for i in range(4,n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]

n = int(input())
ans = []
for i in range(n):
    m = int(input())
    ans.append(sum(m))
for i in ans:
    print(i)