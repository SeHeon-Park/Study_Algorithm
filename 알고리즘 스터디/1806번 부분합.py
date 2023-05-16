import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
l, r = 0, 0
ans = 100001
v = A[0]
while True:
    if v >= m:
        print(l, r)
        ans = min(ans, r-l+1)
        v -= A[l]
        l += 1
    else:
        r += 1
        if r > n - 1:
            break
        v += A[r]

if ans == 100001:
    ans = 0
print(ans)