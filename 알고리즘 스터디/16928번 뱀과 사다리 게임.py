import sys
from collections import deque
input = sys.stdin.readline

M = [int(i) for i in range(101)]
visited = [0 for _ in range(101)]

n, m = map(int, input().split())
Q = deque()

for _ in range(n+m):
    u, v = map(int, input().split())
    M[u] = v
Q.append((1, 0))

while Q:
    u, cnt = Q.popleft()
    if u == 100:
        print(cnt)
        break
    for d in range(1, 7):
        if u+d > 100 or visited[u+d]:
            continue
        visited[u+d] = 1
        Q.append((M[u+d], cnt+1))

