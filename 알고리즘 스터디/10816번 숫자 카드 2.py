import sys
from bisect import bisect_right, bisect_left

input = sys.stdin.readline

n = int(input())
N = [int(x) for x in input().split()]
m = int(input())
M = [[int(x)] for x in input().split()]

ans = [0 for _ in range(m)]
for i in range(m):
    M[i].append(i)

N.sort()
M.sort(key=lambda x:x[0])

for i in M:
    idx_l = bisect_left(N, i[0])
    idx_r = bisect_right(N, i[0])
    if idx_l >= len(N) or N[idx_l] != i[0]:
        ans[i[1]] = 0
        continue
    ans[i[1]] = idx_r-idx_l

for a in ans:
    print(a, end=' ')

