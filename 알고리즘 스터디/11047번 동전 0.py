import sys
input = sys.stdin.readline

def bisect(A, t, r, l=0):
    while l <= r:
        m = (l + r) // 2
        if A[m] == t:
            return m
        elif A[m] < t:
            l = m+1
        else:
            r = m-1
    return r


n, k = map(int, input().split())
C = []
cnt = 0
index = n-1
for _ in range(n):
    C.append(int(input()))

while True:
    if k == 0:
        print(cnt)
        break
    index = bisect(C, k, index)
    if k >= C[index]:
        quotient = k // C[index]
        k -= quotient*C[index]
        cnt += quotient
