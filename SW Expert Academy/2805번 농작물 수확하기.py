T = int(input())

def prefix_sum(h, l, r):
    cnt = 0
    for i in range(l, r+1):
        cnt += M[h][i]
    return cnt

for t in range(T):
    n = int(input())
    M = []
    for _ in range(n):
        M.append(list(map(int, input())))
    u, d = n//2-1, n//2+1
    l, r = 1, n-2
    ans = sum(M[n//2])
    while u>=0:
        ans += (prefix_sum(u, l, r) + prefix_sum(d, l, r))
        l += 1
        r -= 1
        u -= 1
        d += 1
    print("#{} {}".format(t+1, ans))