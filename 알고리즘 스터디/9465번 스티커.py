T = int(input())
for t in range(T):
    n = int(input())
    S = [[0]+[int(x) for x in input().split()],
         [0]+[int(x) for x in input().split()]]
    DP = [[0 for x in range(n+1)],
         [0 for x in range(n+1)]]
    DP[0][1] = S[0][1]
    DP[1][1] = S[1][1]
    for i in range(2, n+1):
        DP[0][i] = max(DP[0][i-2], DP[1][i-2], DP[1][i-1]) + S[0][i]
        DP[1][i] = max(DP[0][i-2], DP[1][i-2], DP[0][i-1]) + S[1][i]
    print(max(DP[0][-1], DP[1][-1]))