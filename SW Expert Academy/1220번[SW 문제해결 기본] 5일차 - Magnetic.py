for t in range(10):
    l = int(input())
    M = []
    for _ in range(l):
        M.append(list(map(int, input().split())))
    ans = 0
    for i in range(l):
        n, s = 0, l - 1
        while True:
            if n>l-1 or M[n][i] == 1:
                break
            n += 1
        if n>l-1:
            continue
        while True:
            if s<0 or M[s][i] == 2:
                break
            s -= 1
        if s<0:
            continue
        status = 1
        for j in range(n, s+1):
            if M[j][i] == 1:
                status = 1
                continue
            if status+M[j][i] == 3:
                ans += 1
                status = 0
    print("#{} {}".format(t+1, ans))