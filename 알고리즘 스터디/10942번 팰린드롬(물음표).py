import sys
input = sys.stdin.readline

n = int(input())
A = [int(x) for x in input().split()]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][i] = 1

if A[0] == A[1]: dp[1][2] = 1
else: dp[1][2] = 0

for i in range(3, n+1):
    for j in range(i-1, 0, -1):
        if i - j == 1:
            if A[i-1] == A[j-1]:
                dp[j][i] = 1
            else:
                dp[j][i] = 0
        else:
            if A[i-1] == A[j-1] and dp[j+1][i-1] == 1:
                dp[j][i] = 1
            else:
                dp[j][i] = 0

m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])





