import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

T = int(input())

n = int(input())
A = [int(x) for x in input().split()]

m = int(input())
B = [int(x) for x in input().split()]

sum_A = []
sum_B = []

idx = n-1
while idx >= 0:
    sum_A.append(A[idx])
    sum = A[idx]
    for i in range(idx-1, -1, -1):
        sum += A[i]
        sum_A.append(sum)
    idx -= 1
sum_A.sort()

idx = m-1
while idx >= 0:
    sum_B.append(B[idx])
    sum = B[idx]
    for i in range(idx-1, -1, -1):
        sum += B[i]
        sum_B.append(sum)
    idx -= 1
sum_B.sort()
ans = 0

for a in sum_A:
    target = T-a
    l = bisect_left(sum_B, target)
    r = bisect_right(sum_B, target)
    ans += (r - l)

print(ans)

