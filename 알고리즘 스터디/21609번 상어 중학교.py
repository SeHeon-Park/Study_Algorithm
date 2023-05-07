import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    T = [] # 종류, 무지개, 기준블록 행, 기준블록 열
    visited1 = [[0 for _ in range(n)] for _ in range(n)]
    Q = deque()
    for i in range(n):
        for j in range(n):
            if visited1[i][j] or M[i][j] <= 0: continue
            visited2 = [[0 for _ in range(n)] for _ in range(n)]
            p = M[i][j]
            temp = [[i, j]]
            visited1[i][j] = 1
            visited2[i][j] = 1
            Q.append((i, j))
            r = 0
            while Q:
                qy, qx = Q.popleft()
                for zx, zy in zip(dx, dy):
                    x = qx + zx
                    y = qy + zy
                    if x<0 or x>n-1 or y<0 or y>n-1 or M[y][x] < 0 or visited2[y][x]: continue
                    if M[y][x] != 0 and M[y][x] != p: continue
                    if M[y][x] == 0:
                        r += 1
                    visited1[y][x] = 1
                    visited2[y][x] = 1
                    temp.append([y, x])
                    Q.append((y, x))
            if len(temp) == 1:
                continue
            T.append([temp, r, j, i])
    T.sort(key=lambda x:(-len(x[0]), -x[1], -x[3], -x[2]))
    return T

def gravity():
    for x in range(n):
        for y in range(n-2, -1, -1):
            if M[y][x] < 0: continue
            prev, next = y, y+1
            while True:
                if next > n-1 or M[next][x] != -2:
                    break
                M[prev][x], M[next][x] = -2, M[prev][x]
                prev += 1
                next += 1

def rotation():
    A = []
    for x in range(n-1, -1, -1):
        temp = []
        for y in range(n):
            temp.append(M[y][x])
        A.append(temp)
    return A




n, m = map(int, input().split())
M = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(n):
    M.append(list(map(int, input().split())))

ans = 0

while True:
    T = bfs()
    if not T: break
    T = T[0][0]
    ans += (len(T) ** 2)
    for t in T:
        M[t[0]][t[1]] = -2
    gravity()
    M = rotation()
    gravity()

print(ans)

