import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
M = []
A = [[[] for _ in range(n)] for _ in range(n)]
Y = [[5 for _ in range(n)] for _ in range(n)]
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

for _ in range(n):
    M.append(list(map(int, input().split())))

for _ in range(m):
    x, y, z = map(int, input().split())
    A[x-1][y-1].append(z)

for _ in range(k):
    ## 봄, 여름
    for i in range(n):
        for j in range(n):
            if A[i][j]:
                T = A[i][j]
                alive = []
                dead = []
                for t in range(len(T)):
                    if T[t] > Y[i][j]:
                         dead.append(T[t])
                    else:
                        Y[i][j] = Y[i][j] - T[t]
                        alive.append(T[t]+1)
                A[i][j] = alive
                ## 여름
                for d in dead:
                    Y[i][j] += d//2
    ## 가을, 겨울
    for i in range(n):
        for j in range(n):
            if A[i][j]:
                T = A[i][j]
                for t in T:
                    if t % 5 == 0:
                        for zx, zy in zip(dx, dy):
                            x = j + zx
                            y = i + zy
                            if x<0 or x>n-1 or y<0 or y>n-1:
                                continue
                            A[y][x].insert(0, 1)

            Y[i][j] += M[i][j]

ans = 0
for tree in A:
    for t in tree:
        ans += len(t)

print(ans)