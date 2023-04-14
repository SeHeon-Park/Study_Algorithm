import sys
from collections import deque
input = sys.stdin.readline

n, m, h = map(int, input().split())
M = []
visited = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(h)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
Q = deque()

for _ in range(h):
    level= []
    for _ in range(m):
        level.append(list(map(int, input().split())))
    M.append(level)

cnt = 0
al = 0
for k in range(h):
    for i in range(m):
        for j in range(n):
            if M[k][i][j] == 1:
                Q.append((k, i, j))
                cnt += 1
                al += 1
                visited[k][i][j] = 1
            if M[k][i][j] == 0:
                al += 1

if al == len(Q):
    print(0)
else:
    time = 0
    cnt2, cnt3 = 0, 0
    temp = 0
    while Q:
        qh, qy, qx = Q.popleft()
        cnt2 += 1
        temp += 1

        # 앞, 뒤
        if qh+1 <= h-1 and M[qh+1][qy][qx] == 0:
            M[qh+1][qy][qx] = 1
            cnt3 += 1
            Q.append((qh+1, qy, qx))

        if qh-1 >= 0 and M[qh-1][qy][qx] == 0:
            M[qh-1][qy][qx] = 1
            cnt3 += 1
            Q.append((qh-1, qy, qx))

        for zx, zy in zip(dx, dy):
            x = qx+zx
            y = qy+zy
            if x<0 or x>n-1 or y<0 or y>m-1 or M[qh][y][x] != 0:
                continue
            M[qh][y][x] = 1
            cnt3 += 1
            Q.append((qh, y, x))

        if cnt == cnt2:
            time += 1
            cnt2 = 0
            cnt = cnt3
            cnt3 = 0

    if al != temp:
        print(-1)
    else:
        print(time-1)
