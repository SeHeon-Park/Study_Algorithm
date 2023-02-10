import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
I = [0]
A = [int(x) for x in input().split()]
D = [A[0]]

m = 0
t = 0
for i in range(1, n):
    if D[-1] < A[i]:
        D.append(A[i])
        I.append(len(D)-1)
        if m < len(D)-1:
            m = len(D)-1
            t = len(I)-1
        continue
    idx = bisect_left(D, A[i])
    I.append(idx)
    D[idx] = A[i]

cnt = 0
ans = []
for i in range(t, -1, -1):
    if I[i] == m:
        ans.append(A[i])
        m -= 1

print(len(ans))
for i in range(len(ans)-1, -1, -1):
    print(ans[i], end=" ")