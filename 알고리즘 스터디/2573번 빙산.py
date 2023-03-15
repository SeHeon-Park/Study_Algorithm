import sys
from collections import deque
input = sys.stdin.readline

def water_cnt():
    for i in range(n):
        for j in range(m):
            if M[i][j]:
                cnt = 0
                for zx, zy in zip(dx, dy):
                    x = j + zx
                    y = i + zy
                    if x<0 or x>m-1 or y<0 or y>n-1 or M[y][x]:
                        continue
                    cnt += 1
                C[i][j] = cnt

def bfs():
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if M[i][j] and not visited[i][j]:
                cnt += 1
                Q.append((j, i))
                visited[i][j] = 1
                while Q:
                    qx, qy = Q.popleft()
                    for zx, zy in zip(dx, dy):
                        x = qx + zx
                        y = qy + zy
                        if x<0 or x>m-1 or y<0 or y>n-1 or not M[y][x] or visited[y][x]:
                            continue
                        visited[y][x] = 1
                        Q.append((x, y))
    return cnt

n, m = map(int, input().split())
M = []
C = [[0 for _ in range(m)] for _ in range(n)]
Q = deque()

for _ in range(n):
    M.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

water_cnt()

time = 1

while True:
    for i in range(n):
        for j in range(m):
            if M[i][j]:
                temp = M[i][j] - C[i][j]
                if temp <= 0:
                    M[i][j] = 0
                else:
                    M[i][j] = temp
    water_cnt()

    cnt = bfs()
    if cnt >= 2:
        print(time)
        break
    if cnt == 0:
        print(0)
        break
    time += 1

