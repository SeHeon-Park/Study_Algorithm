# import sys
# input = sys.stdin.readline

n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input())))

if n == 1 or m == 1:
    print(1)
else:
    DP = [[0 for _ in range(m)] for _ in range(n)]
    ans = 0
    for i in range(m):
        if A[0][i] == 1:
            ans = 1
        DP[0][i] = A[0][i]

    for i in range(n):
        if A[i][0] == 1:
            ans = 1
        DP[i][0] = A[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if A[i][j] == 1:
                DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1]) + 1
                if DP[i][j] > ans:
                    ans = DP[i][j]
    print(ans*ans)
