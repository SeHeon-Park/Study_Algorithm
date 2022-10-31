def check_w(i, j):
    l, r = j, j+n-1
    while l <= r:
        if M[i][l] != M[i][r]:
            return False
        l += 1
        r -= 1
    return True


def check_h(i, j):
    l, r = i, i+n-1
    while l <= r:
        if M[l][j] != M[r][j]:
            return False
        l += 1
        r -= 1
    return True


for t in range(10):
    n = int(input())
    M = []
    cnt = 0
    for _ in range(8):
        M.append(input())
    for i in range(8):
        for j in range(8):
            if j<=8-n and check_w(i, j):
                cnt += 1
            if i<=8-n and check_h(i, j):
                cnt += 1
    print("#{} {}".format(t+1, cnt))
