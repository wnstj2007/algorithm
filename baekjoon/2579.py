def stair(scores):
    n = len(scores)
    if n==1:
        return scores[0]
    dp = [0 for i in range(n)]
    dp[0] = scores[0]
    dp[1] = dp[0]+scores[1]
    for i in range(2, n):
        dp[i] = max(dp[i-2]+scores[i], dp[i-3]+scores[i]+scores[i-1])
    return dp[n-1]

n = int(input())
scores = []
for i in range(n):
    scores.append(int(input()))
print(stair(scores))