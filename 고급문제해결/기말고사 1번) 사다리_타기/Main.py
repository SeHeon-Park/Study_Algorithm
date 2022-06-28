n, m = map(int, input().split())
A = [int(i) for i in input().split()]
M = []
for i in range(m):
    M.append([int(i) for i in input().split()])
M.sort(key=lambda x : x[1])
for m in M:
    temp = A[m[0]]
    A[m[0]] = A[m[0]+1]
    A[m[0] + 1] = temp
print(A[n//2])