import sys
from math import factorial
input = sys.stdin.readline


n, r, g, b = map(int, input().split())
max_o = 0
if n % 2:
    max_o = n
else:
    max_o = n-1

dp = [[[[0 for _ in range(b+1)] for _ in range(g+1)] for _ in range(r+1)] for _ in range(n+1)]

# 1층 해결
dp[1][0][0][1] = 1
dp[1][1][0][0] = 1
dp[1][0][1][0] = 1


for l in range(2, n+1):
    # 1개의 색깔
    if len(dp[1])>l:
        dp[l][l][0][0] = dp[l][l][0][0] + 1
    if len(dp[l][0])>l:
        dp[l][0][l][0] = dp[l][0][l][0] + 1
    if len(dp[l][0][0]) > l:
        dp[l][0][0][l] = dp[l][0][0][l] + 1

    if l % 2 == 0:
        c = l//2 # c개 만큼 2개의 색깔 사용 가능
        v = factorial(l)//(factorial(c)*factorial(c))
        # g, b
        if len(dp[l][0])>c and len(dp[l][0][0]):
            for i in range(1, r+1):
                dp[l][i][c][c] = dp[l][i][c][c] + v
        # r, g
        if len(dp[l])>c and len(dp[l][0])>c:
            for i in range(1, b+1):
                dp[l][c][c][i] = dp[l][c][c][i] + v
        # r, b
        if len(dp[l]) > c and len(dp[l][0][0]) > c:
            for i in range(1, g+1):
                dp[l][c][i][c] = dp[l][c][i][c] + v
    if l % 3 == 0:
        c = l//3 # c개 만큼 3개의 색깔 사용 가능
        v = factorial(l) // (factorial(c) * factorial(c))
        print(c, l)
        # g, b
        if len(dp[l])>c and len(dp[l][0])>c and len(dp[l][0][0]):
            dp[l][c][c][c] = dp[l][c][c][c] + v



for d in dp:
    print(d)
ans = 0

print(ans)
