from collections import deque
import math

T = int(input())
for t in range(T):
    n = int(input())
    M = []
    Q = deque()
    for _ in range(n):
        M.append(list(map(int, input().split())))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    ans = -math.inf
    num = 0
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            Q.append((j, i, 1))
            visited[i][j] = 1
            while Q:
                qx, qy, cnt = Q.popleft()
                for zx, zy in zip(dx, dy):
                    x = qx + zx
                    y = qy + zy
                    if x < 0 or x > n - 1 or y < 0 or y > n - 1 or M[y][x] - M[qy][qx] != 1:
                        continue
                    if M[y][x] - M[qy][qx] != 1:
                        continue
                    visited[y][x] = 1
                    Q.append((x, y, cnt+1))
            if ans < cnt:
                ans, num = cnt, M[i][j]
            elif ans == cnt and num > M[i][j]:
                ans, num = cnt, M[i][j]

    print("#{} {} {}".format(t+1, num, ans))