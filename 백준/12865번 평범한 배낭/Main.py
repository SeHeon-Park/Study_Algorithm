n, k = map(int, input().split())
item = [[0, 0]]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    w, v = map(int, input().split())
    item.append([w, v])

for i in range(1, n+1):
    for j in range(1, k+1):
        if item[i][0] <= j:
            dp[i][j] = max(item[i][1] + dp[i-1][j-item[i][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])


