import math, copy
from collections import deque
from itertools import permutations

def make_number(A):
    result, temp = 0, 1
    for a in range(len(A)-1, -1, -1):
        result += A[a] * temp
        temp *= 10
    return result

t = int(input())

for i in range(t):
    Q = deque()
    ans = -math.inf
    n, c = map(int, input().split())
    N = list(map(int, str(n))) + [0]
    P = [int(i) for i in range(len(N)-1)]
    S = set()
    Q.append(N)
    while Q:
        T = Q.popleft()
        if T[-1] == c:
            ans = max(ans, make_number(T[:-1]))
            continue
        for p in permutations(P, 2):
            if T[p[0]] > T[p[1]]:
                continue
            B = copy.deepcopy(T)
            B[p[0]], B[p[1]] = B[p[1]], B[p[0]]
            B[-1] = B[-1] + 1
            if tuple(B) not in S:
                S.add(tuple(B))
                Q.append(B)
    print("#{} {}".format(i+1, ans))