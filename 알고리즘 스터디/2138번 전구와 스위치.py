## 첫번째 전구를 키는 경우, 안키는 경우에 따라 경우의 수가 나뉜다..

import copy

n = int(input())
A = list(map(int, input()))
B = list(map(int, input()))
cnt = 0

def reverse(i):
    if i == n-2:
        A[i] = abs(A[i]-1)
        A[i+1] = abs(A[i+1]-1)
    else:
        A[i] = abs(A[i]-1)
        A[i+1] = abs(A[i+1]-1)
        A[i+2] = abs(A[i+2]-1)

C = copy.deepcopy(A)

for i in range(n-1):
    if A[i] != B[i]:
        reverse(i)
        cnt += 1
if A == B:
    print(cnt)
else:
    cnt = 1
    A = copy.deepcopy(C)
    A[0] = abs(A[0]-1)
    A[1] = abs(A[1]-1)
    for i in range(n - 1):
        if A[i] != B[i]:
            reverse(i)
            cnt += 1
    if A == B:
        print(cnt)
    else:
        print(-1)
