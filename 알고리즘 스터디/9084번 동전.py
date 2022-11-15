T = int(input())
for t in range(T):
    n = int(input())
    C = [int(x) for x in input().split()]
    target = int(input())
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for c in C:
        for i in range(c, target+1):
            if i < c:
                continue
            dp[i] += dp[i-c]
    print(dp[-1])