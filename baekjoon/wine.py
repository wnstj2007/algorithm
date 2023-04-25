def drink(wines):
    n = len(wines)
    dp = [0 for i in range(n)]
    dp[0] = wines[0]
    if len(dp) > 1:
        dp[1] = wines[0] + wines[1]
    for i in range(2,n):
        wine = wines[i]
        dp[i] = max(dp[i-2]+wine, dp[i-3]+wine+wines[i-1])
        dp[i] = max(dp[i-1], dp[i])
    return max(dp)

n = int(input())
wines = []
for i in range(n):
    wines.append(int(input()))
print(drink(wines))