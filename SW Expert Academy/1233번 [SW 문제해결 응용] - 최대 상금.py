def dfs(idx, cnt):
    global ans
    if cnt == 0:
        s = ""
        for m in M:
            s += str(m)
        ans = max(ans, int(s))
        return

    if idx > len(M)-1:
        s = ""
        flag = 0
        for i in range(len(M)-1):
            if flag:
                break
            for j in range(i+1, len(M)):
                if M[i] == M[j]:
                    flag = 1
                    break

        if flag or cnt % 2 == 0:
            for m in M:
                s += str(m)
        else:
            for i in range(len(M)-2):
                s += str(M[i])
            s += (str(M[-1]) + str(M[-2]))
        ans = max(ans, int(s))
        return

    p = M[idx]
    for i in range(idx+1, len(M)):
        if p < M[i]:
            p = M[i]

    if p != M[idx]:
        for i in range(idx+1, len(M)):
            if p == M[i]:
                M[idx], M[i] = M[i], M[idx]
                dfs(idx+1, cnt-1)
                M[idx], M[i] = M[i], M[idx]
    else:
        dfs(idx+1, cnt)


T = int(input())
for t in range(1, T+1):
    n, c = map(int, input().split())
    M = list(str(n))
    ans = 0
    for i in range(len(M)):
        M[i] = int(M[i])
    dfs(0, c)
    print("#{0} {1}".format(t, ans))