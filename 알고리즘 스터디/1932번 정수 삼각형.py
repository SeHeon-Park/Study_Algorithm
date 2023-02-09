import sys
input = sys.stdin.readline

n = int(input())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(A[i])):
        if j == 0: A[i][j] += A[i-1][j]
        elif j == len(A[i])-1: A[i][j] += A[i-1][-1]
        else: A[i][j] += max(A[i-1][j-1], A[i-1][j])

print(max(A[-1]))


