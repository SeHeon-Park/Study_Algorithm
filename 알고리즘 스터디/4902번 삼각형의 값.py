import sys, math
input = sys.stdin.readline

answer = []
n = -1

while True:
    T, S, pre, pre_T = [], [], [], []
    ans = -math.inf
    M = list(map(int, input().split()))
    n = M[0]
    if n == 0:
        break
    l = (n * (2 + (n - 1) * 2)) // 2
    cnt = 1
    for i in range(1, l + 1):
        T.append(M[i])
        pre_T.append(sum(T))
        if len(T) == cnt:
            S.append(T)
            pre.append(pre_T)
            T, pre_T = [], []
            cnt += 2
    # 정삼각형 기준
    height = 0
    while height != n:
        for i in range(0, len(S[height]), 2):
            l, r, temp = i, i+2, S[height][i]
            ans = max(ans, temp)
            for j in range(height+1, n):
                if l<0 or r>len(S[j])-1:
                    break
                if l == 0:
                    temp += pre[j][r]
                else:
                    temp += (pre[j][r] - pre[j][l-1])
                ans = max(ans, temp)
                r += 2
        height += 1

    # 역삼각형 기준
    height = n-1
    while height != -1:
        l, r = 0, 0
        for i in range(3, len(S[height])-3, 2):
            l, r = i-2, i
            temp = S[height][i]
            ans = max(ans, temp)
            for j in range(height-1, 1, -1):
                if l < 0 or r > len(S[j])-1:
                    break
                temp += (pre[j][r] - pre[j][l-1])
                ans = max(ans, temp)
                l -= 2
        height -= 1

    answer.append(ans)

for i in range(len(answer)):
    print("{}. {}".format(i+1, answer[i]))
