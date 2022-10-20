from collections import deque
import math

T = int(input())

for t in range(T):
    n = int(input())
    M = []
    for _ in range(n):
        M.append(list(map(int, input())))
    N = [[math.inf for _ in range(n)] for _ in range(n)]
    Q = deque()
    Q.append((0, 0, M[0][0]))
    ans = math.inf
    while Q:
        I = Q.popleft()
        if I[2] >= ans:
            continue
        if I[0] == n-1 and I[1] == n-1:
            ans = min(N[n-1][n-1], I[2])
            continue
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for zx, zy in zip(dx, dy):
            x = I[0] + zx
            y = I[1] + zy
            if x<0 or x>n-1 or y<0 or y>n-1:
                continue
            if N[y][x] > I[2]+M[y][x]:
                N[y][x] = I[2]+M[y][x]
                Q.append((x, y, I[2]+M[y][x]))
    print("#{} {}".format(t+1, ans))