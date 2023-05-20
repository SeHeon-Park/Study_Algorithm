import sys
input = sys.stdin.readline

t, w = map(int, input().split())
A = []
dp = [[0 for _ in range(t+1)] for _ in range(w+1)]
W = [0 for _ in range(w+1)]

for _ in range(t):
    A.append(int(input()))

for i in range(w+1):
    if i % 2 == 0:
        W[i] = 1
    else:
        W[i] = 2

cnt = 0
for i in range(1, t+1):
    if A[i-1] == 1:
        cnt += 1
    dp[0][i] = cnt


for i in range(1, t+1):
    for j in range(1, w+1):
        # 받아 먹을 때
        if W[j] == A[i-1]:
            dp[j][i] = max(dp[j][i-1], dp[j-1][i-1]) + 1
        # 못 받아 먹을 때
        else:
            dp[j][i] = max(dp[j][i-1], dp[j-1][i-1])

ans = 0
for d in dp:
    ans = max(ans, max(d))

print(ans)