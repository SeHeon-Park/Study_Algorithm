import sys
import copy
from collections import deque

input = sys.stdin.readline

I = list(map(int, input().split()))
I.sort()
Q = deque()
S = set()
Q.append(I)
S.add((I[0], I[1], I[2]))
flag = 0

while Q:
    A = Q.popleft()
    if A[0] == A[1] == A[2]:
        print(1)
        flag = 1
        break
    for i in range(2):
        for j in range(i+1, 3):
            T = copy.deepcopy(A)
            x, y = T[i], T[j]
            T[i] = x+x
            T[j] = y-x
            T.sort()
            if (T[0], T[1], T[2]) not in S:
                S.add((T[0], T[1], T[2]))
                Q.append(T)

if not flag:
    print(0)