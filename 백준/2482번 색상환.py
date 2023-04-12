# n번째 색을 포함하고 k개 고르기 = n-2개의 색을 가지고 k-1개 고르기
# n번째 색을 포함하지 않고 k개 고르기 = n-1번째 색을 가지고 k개 고르기
# -> 이해 안감

# 내 생각은 이거다!
# n번째 색을 포함하고 k개 고르기 = (n-2개의 색을 가지고 k-1개 고르기)-1 (1과 n이 인접하므로)
# n번째 색을 포함하지 않고 k개 고르기 = (n-1번째 색을 가지고 k개 고르기)+1 (n이 있음, (1)<->(n-1) 경우가 추가됨)
# -> dp[n][k] = (dp[n-2][k-1]-1) + (dp[n-1][k]+1)

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

if k == 1:
    print(n)
else:
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    dp[3][1] = 3
    dp[4][1] = 4
    dp[4][2] = 2

    for i in range(5, n+1):
        dp[i][1] = i
        for j in range(2, k+1):
            dp[i][j] = dp[i-2][j-1] + dp[i-1][j]

    print(dp[-1][-1]%1000000003)

