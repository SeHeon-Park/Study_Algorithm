n = int(input())
if not n:
    print(0)
else:
    DP = [0 for _ in range(n+1)]
    DP[1] = 1
    for i in range(2, n+1):
        DP[i] = DP[i-1] + DP[i-2]
    print(DP[n])