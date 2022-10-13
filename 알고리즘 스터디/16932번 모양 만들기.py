import sys, math
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
M = []
ans = -math.inf
dic = {}
idx = 1
Q = deque()

for _ in range(n):
    M.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]
N = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if M[i][j] == 1 and not visited[i][j]:
            P = []
            visited[i][j] = 1
            Q.append((i, j))
            cnt = 1
            while Q:
                qy, qx = Q.popleft()
                P.append((qy, qx))
                dx = [0, 1, 0, -1]
                dy = [1, 0, -1, 0]
                for zx, zy in zip(dx, dy):
                    x = qx + zx
                    y = qy + zy
                    if x<0 or x>m-1 or y<0 or y>n-1 or visited[y][x]:
                        continue
                    if M[y][x] == 1:
                        cnt += 1
                        visited[y][x] = 1
                        Q.append((y, x))
            for p in P:
                N[p[0]][p[1]] = idx
                dic[idx] = cnt
            idx += 1

for i in range(n):
    for j in range(m):
        if M[i][j] == 0:
            S = set()
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            for zx, zy in zip(dx, dy):
                x = j + zx
                y = i + zy
                if x < 0 or x > m - 1 or y < 0 or y > n - 1:
                    continue
                if M[y][x] == 1:
                    S.add(N[y][x])
            if S:
                a = 0
                for s in S:
                    a += dic[s]
                ans = max(ans, a+1)
print(ans)
