n = int(input())
M = list(map(int, input().split()))
A = [0 for _ in range(n)]
A[0] = M[0]

for i in range(1, n):
    A[i] = max(M[i], A[i-1]+M[i])

print(max(A))
