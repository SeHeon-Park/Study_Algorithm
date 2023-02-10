import sys
input = sys.stdin.readline

n = int(input())
S = []
for _ in range(n):
    S.append(int(input()))
if n == 1:
    print(S[0])
else:
    DP = [[0, 0] for _ in range(n)]
    DP[0][1] = S[0]
    DP[1][0] = S[1]
    DP[1][1] = S[0]+S[1]

    for i in range(2, n):
        DP[i][0] = max(DP[i-2][0], DP[i-2][1]) + S[i]
        DP[i][1] = DP[i-1][0] + S[i]

    print(max(DP[-1]))

