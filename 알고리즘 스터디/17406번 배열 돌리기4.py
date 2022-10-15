import sys, math, copy
from itertools import permutations
input = sys.stdin.readline

def rotation(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return
    lu = B[y1][x1]
    ld = B[y2][x2]
    for i in range(y2-y1):
        B[y1 + i][x1] = B[y1 + 1 + i][x1]
        B[y2 - i][x2] = B[y2 - 1 - i][x2]
    for i in range(x2-x1-1):
        B[y2][x1 + i] = B[y2][x1 + 1 + i]
        B[y1][x2 - i] = B[y1][x2 - 1 - i]
    B[y1][x1 + 1] = lu
    B[y2][x2 - 1] = ld
    rotation(x1+1, y1+1, x2-1, y2-1)
    return

n, m, k = map(int, input().split())
A, R = [], []
ans = math.inf
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(k):
    R.append(list(map(int, input().split())))

for r in permutations(R, len(R)):
    B = copy.deepcopy(A)
    for i in r:
        rotation(i[1]-i[2]-1, i[0]-i[2]-1, i[1]+i[2]-1, i[0]+i[2]-1)
    for b in B:
        ans = min(ans, sum(b))

print(ans)