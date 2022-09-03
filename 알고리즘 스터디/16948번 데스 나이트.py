import sys
from collections import deque
input = sys.stdin.readline


def can_go(r, c):
    if r >= n or r <= -1 or c >= n or c <= -1 or visited[r][c]:
        return False
    return True

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

visited = [[0 for _ in range(n)] for _ in range(n)]
Q = deque()
dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

for zr, zc in zip(dr, dc):
    r = r1 + zr
    c = c1 + zc
    if not can_go(r, c):
        continue
    visited[r][c] = 1
    Q.append((r, c, 1))

while Q:
    qr, qc, cnt = Q.popleft()
    if qr == r2 and qc == c2:
        print(cnt)
        break
    for zr, zc in zip(dr, dc):
        r = qr + zr
        c = qc + zc
        if not can_go(r, c):
            continue
        visited[r][c] = 1
        Q.append((r, c, cnt+1))

if not Q:
    print(-1)