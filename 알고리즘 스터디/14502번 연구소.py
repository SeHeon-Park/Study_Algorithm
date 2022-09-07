import sys
import copy
import math
from collections import deque

input = sys.stdin.readline


def bfs():
    cnt = 0
    N = copy.deepcopy(M)
    visited = [[0 for _ in range(m)] for _ in range(n)]
    du = [0, 1, 0, -1]
    dv = [1, 0, -1, 0]
    for i in range(n):
        for j in range(m):
            if M[i][j] == 2:
                Q.append((i, j))
    while Q:
        qu, qv = Q.popleft()
        for zu, zv in zip(du, dv):
            u = qu + zu
            v = qv + zv
            if 0 <= u < n and 0 <= v < m and N[u][v] == 0 and not visited[u][v]:
                N[u][v] = 2
                visited[u][v] = 1
                Q.append((u, v))
    cnt += N.count(0)
    return cnt


def make_wall(cnt):
    global maximum
    if cnt == 3:
        maximum = max(maximum, bfs())
        return
    for i in range(n):
        for j in range(m):
            if M[i][j] == 0:
                M[i][j] = 1
                make_wall(cnt + 1)
                M[i][j] = 0


n, m = map(int, input().split())
M = [[int(x) for x in input().split()] for _ in range(n)]
Q = deque()
maximum = -math.inf

make_wall(0)

print(maximum)