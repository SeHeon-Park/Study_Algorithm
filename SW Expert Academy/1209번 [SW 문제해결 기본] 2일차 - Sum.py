for _ in range(10):
    t = int(input())
    M = []
    for _ in range(100):
        M.append(list(map(int, input().split())))
    ans = 0
    for i in range(100):
        col, row = 0, 0
        for j in range(100):
            col += M[j][i]
            row += M[i][j]
        ans = max(ans, col, row)

    lc, rc, idx_l, idx_r = 0, 0, 0, 99
    for i in range(100):
        lc += M[i][idx_l]
        rc += M[i][idx_r]
        idx_l += 1
        idx_r -= 1
    ans = max(ans, lc, rc)
    print("#{} {}".format(t, ans))