import sys
input = sys.stdin.readline

def bisect_left(target):
    l, r = 0, n*n-1
    while l < r:
        m = (l+r)//2
        if M2[m] < target:
            l = m+1
        else:
            r = m
    return l

def bisect_right(target):
    l, r = 0, n*n-1
    while l < r:
        m = (l+r)//2
        if M2[m] > target:
            r = m
        else:
            l = m+1
    return l


n = int(input())
M = []
A, B, C, D = [], [], [], []
M1, M2 = [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for a in A:
    for b in B:
        M1.append(a+b)

for c in C:
    for d in D:
        M2.append(c+d)

M1.sort()
M2.sort()
ans = 0

for m in M1:
    ans += (bisect_right(-m)-bisect_left(-m))

print(ans)



