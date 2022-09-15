def reverse(a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            A[i][j] = abs(A[i][j]-1)

n, m = map(int, input().split())
cnt = 0
A, B = [], []

for _ in range(n):
    A.append(list(map(int, input())))

for _ in range(n):
    B.append(list(map(int, input())))

for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            reverse(i, j)
            cnt += 1
        if A == B:
            break

if A == B:
    print(cnt)
else:
    print(-1)