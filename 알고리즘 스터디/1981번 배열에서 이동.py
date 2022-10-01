## bfs를 수행하며 매번 max, min연산을 통해 최대, 최소를 구하는 방식은 시간초과..
## 모든 범위를 구해서 bfs를 수행하는 방식을 채택

import sys
import math
from collections import deque
input = sys.stdin.readline

def bfs(m, left, right):
    if M[0][0]<left or M[0][0]>right:
        return False
    Q = deque()
    Q.append((0, 0))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[0][0] = 1
    while Q:
        u, v = Q.popleft()
        if u == n-1 and v == n-1:
            return True
        for zx, zy in zip(dx, dy):
            x = u + zx
            y = v + zy
            if 0<=x<=n-1 and 0<=y<=n-1 and not visited[y][x] and left<=M[y][x]<=right:
                Q.append((x, y))
                visited[y][x] = 1
    return False

n = int(input())
M = []
temp_min, temp_max = math.inf, -math.inf
for _ in range(n):
    a = list(map(int, input().split()))
    M.append(a)
    temp_min, temp_max = min(min(a), temp_min), max(max(a), temp_max)

l, r = 0, temp_max - temp_min

while l<=r:
    flag = 0
    m = (l + r) // 2
    for i in range(temp_max-m+1):
        if bfs(m, i, i+m):
            ans = m
            r = m-1
            flag = 1
            break
    if not flag:
        l = m+1
        flag = 0

print(ans)