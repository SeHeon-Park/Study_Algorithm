import sys
input = sys.stdin.readline

n, m = map(int, input().split())
M = [int(x) for x in input().split()]
for i in range(1, n):
    M[i] = M[i]+M[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    if i == 1: print(M[j-1])
    else: print(M[j-1]-M[i-2])