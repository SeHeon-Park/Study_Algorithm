import sys
import math
from collections import deque

input = sys.stdin.readline

def bfs(mid, u):
    Q = deque()
    Q.append(u)
    visited = [0 for _ in range(n+1)]
    while Q:
        u = Q.popleft()
        if u == v:
            return True
        for m in M[u]:
            if m[1] >= mid and not visited[m[0]]:
                visited[m[0]] = 1
                Q.append(m[0])
    return False


n, m = map(int, input().split())
M = [[] for _ in range(n+1)]
l, r = math.inf, -math.inf

for i in range(m):
    a, b, c = map(int, input().split())
    M[a].append((b, c))
    M[b].append((a, c))
    l, r = min(l, c), max(r, c)

u, v = map(int, input().split())

while l < r+1:
    mid = (l+r)//2
    if bfs(mid, u):
        ans = mid
        l = mid+1
    else:
        r = mid-1

print(ans)




