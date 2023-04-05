import sys
input = sys.stdin.readline

def move(start, end):
    if start == 0:
        return 2
    if abs(end-start) == 1 or abs(end-start) == 3:
        return 3
    if abs(end-start) == 2:
        return 4
    return 1

M = [int(x) for x in input().split()]
dp = [[[int(1e9) for _ in range(5)] for _ in range(5)] for _ in range(len(M))]
dp[0][M[0]][0] = 2
dp[0][0][M[0]] = 2

for k in range(1, len(M)):
    target = M[k]
    if target == 0:
        break
    for i in range(5):
        for j in range(5):
            if dp[k-1][i][j] == int(1e9):
                continue
            dp[k][target][j] = min(dp[k][target][j], dp[k-1][i][j]+move(i, target))
            dp[k][i][target] = min(dp[k][i][target], dp[k-1][i][j]+move(j, target))


ans = int(1e9)
for d in dp[-2]:
    for a in d:
        ans = min(ans, a)

print(ans)