import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
M, W = [], []

for _ in range(r):
    M.append(list(map(str, input())))

visited = [[0 for _ in range(c)] for _ in range(r)]
Q = deque()

wolf = 0
sheep = 0
flag = 0

for i in range(r):
    for j in range(c):
        if M[i][j] == 'W':
            Q.append((i, j))
            visited[i][j] = 1
            wolf = 1
        if M[i][j] == 'S':
            sheep = 1

if sheep and wolf:
    while Q:
        if flag:
            break
        qy, qx = Q.popleft()
        if M[qy][qx] == 'D':
            continue
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for zx, zy in zip(dx, dy):
            x = qx + zx
            y = qy + zy
            if x<0 or x>c-1 or y<0 or y>r-1 or visited[y][x]:
                continue
            if M[qy][qx] == 'W' and M[y][x] == 'S':
                flag = 1
                break
            if M[y][x] == 'S':
                M[qy][qx] = 'D'
                continue
            visited[y][x] = 1
            Q.append((y, x))
            
    if flag:
        print(0)
    else:
        print(1)
        for m in M:
            for a in m:
                print(a, end="")

else:
    print(1)
    for m in M:
        for a in m:
            print(a, end="")
