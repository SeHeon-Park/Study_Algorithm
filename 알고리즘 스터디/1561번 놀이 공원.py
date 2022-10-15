import sys
input = sys.stdin.readline

n, m = map(int, input().split())
T = [int(x) for x in input().split()]
time = 0

if n <= m:
    print(n)
else:
    l, r = 0, 60000000000
    while l <= r:
        mid = (l+r)//2
        s = 0
        for t in T:
            s += (mid//t)
        if s+m >= n:
            time = mid
            r = mid - 1
        else:
            l = mid + 1
    cnt = m
    ans = []
    for t in range(m):
        a = time // T[t]
        b = time % T[t]
        if b == 0:
            cnt += (a-1)
            ans.append(t+1)
        else:
            cnt += a
    print(ans[n-cnt-1])