import sys
input = sys.stdin.readline

t = int(input())

dp = ["1"*50 for _ in range(101)]
dp[2] = "1"
dp[3] = "7"
dp[4] = "4"
dp[5] = "2"
dp[6] = "6"
dp[7] = "8"

for i in range(8, 101):
    for j in range(i - 2, 1, -1):
        a, b = j, i - j
        num = dp[a] + dp[b]
        if b == 6:
            num = num[:-1]+"0"
        dp[i] = str(min(int(dp[i]), int(num)))

for _ in range(t):
    n = int(input())
    n_max = 0

    # 최대값 구하기
    temp_max = n // 2
    if n % 2 == 0:
        for k in range(temp_max):
            n_max += (10 ** k)
    else:
        for k in range(temp_max - 1):
            n_max += (10 ** k)
        n_max += (10 ** (temp_max - 1)) * 7
    print(dp[n], n_max)




