import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
M = list(map(int, input().split()))

A = [M[0]]
tracing = [0]
for i in range(1, n):
    idx = bisect_left(A, M[i])
    tracing.append(idx)
    if idx > len(A)-1:
        A.append(M[i])
    else:
        A[idx] = M[i]

print(n - len(A))

## 가장 긴 순열도 찾기
ans = []
temp = len(A)-1
for i in range(len(tracing)-1, -1, -1):
    if tracing[i] == temp:
        ans.append(M[tracing[i]])
        temp -= 1

print(list(reversed(ans)))