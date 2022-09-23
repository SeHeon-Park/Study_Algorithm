import sys
from bisect import bisect_left, bisect_right
import math

input = sys.stdin.readline

n = int(input())
M = []
m = -math.inf

for i in range(n):
    M.append(int(input()))

M = sorted(M)
S = set(M)
S = sorted(S)
ans = M[0]

for s in S:
    idx_l = bisect_left(M, s)
    idx_r = bisect_right(M, s)
    if m < idx_r - idx_l:
        ans = M[idx_l]
        m = idx_r - idx_l

print(ans)