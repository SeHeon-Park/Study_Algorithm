import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    info = input().split()
    A, B, T = info[0], info[1], info[2]
    dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
    if A[0] == T[0]:
        dp[0][1] = 1
        for i in range(2, len(A)+1):
            if A[i-1] != T[i-1]:
                break
            dp[0][i] = 1
    if B[0] == T[0]:
        dp[1][0] = 1
        for i in range(2, len(B)+1):
            if B[i-1] != T[i-1]:
                break
            dp[i][0] = 1

    for i in range(1, len(B)+1):
        for j in range(1, len(A)+1):
            if dp[i-1][j] and B[i-1] == T[i+j-1]:
                dp[i][j] = 1
                continue
            if dp[i][j-1] and A[j-1] == T[i+j-1]:
                dp[i][j] = 1


    if dp[len(B)][len(A)]:
        print('Data set {}: yes'.format(t))
    else:
        print('Data set {}: no'.format(t))
