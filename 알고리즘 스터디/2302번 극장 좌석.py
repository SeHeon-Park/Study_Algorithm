import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
S = set()
dp = [0 for _ in range(n)]

for _ in range(m):
    S.add(int(input())-1)

dp[0] = 1
if n>1:
    if 1 in S or 0 in S:
        dp[1] = 1
    else:
        dp[1] = 2

for i in range(2, n):
    if i in S:
        dp[i] = dp[i-1]
        continue
    if i-1 in S:
        dp[i] = dp[i-1]
        continue
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n-1])

