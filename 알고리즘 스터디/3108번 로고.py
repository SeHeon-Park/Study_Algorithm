import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[y][x] = 1
    while Q:
        qx, qy = Q.popleft()
        for zx, zy in zip(dx, dy):
            x = qx + zx
            y = qy + zy
            if x<0 or x>2000 or y<0 or y>2000 or visited[y][x] or not M[y][x]:
                continue
            visited[y][x] = 1
            Q.append((x, y))


def make_map(x1, y1, x2, y2):
    for x in range(x1, x2+1):
        M[y1][x] = 1
        M[y2][x] = 1
    for y in range(y1, y2+1):
        M[y][x1] = 1
        M[y][x2] = 1

n = int(input())
M = [[0 for _ in range(2001)] for _ in range(2001)]
S = set()
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    make_map(2*(x1+500), 2*(y1+500), 2*(x2+500), 2*(y2+500))
    S.add((2*(x1+500), 2*(y1+500)))

ans = 0
visited = [[0 for _ in range(2001)] for _ in range(2001)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


for s in S:
    if visited[s[1]][s[0]] == 1:
        continue
    bfs(s[0], s[1])
    ans += 1

if visited[1000][1000]:
    ans -= 1
print(ans)