import math

n = int(input())
A = [int(i) for i in input().split()]

A.sort()

m = math.inf
l, r = 0, len(A)-1
while l < r:
    m = min(m, A[l]+A[r])
    l += 1
    r -= 1
print(m)