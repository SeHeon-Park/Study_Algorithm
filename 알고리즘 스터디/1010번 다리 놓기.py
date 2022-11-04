T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    DP = m
    for i in range(1, n):
        m -= 1
        DP = DP*m//(i+1)
    print(DP)