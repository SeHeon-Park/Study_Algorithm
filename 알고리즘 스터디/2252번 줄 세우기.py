import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
M = [0 for _ in range(n+1)]
dic = defaultdict(list)
ans = []
Q = deque()

for _ in range(m):
    u, v = map(int, input().split())
    M[v] += 1
    dic[u].append(v)

for i in range(1, n+1):
    if not M[i]:
        Q.append(i)

while Q:
    u = Q.popleft()
    ans.append(u)
    for v in dic[u]:
        M[v] -= 1
        if not M[v]:
            Q.append(v)

print(*ans)

