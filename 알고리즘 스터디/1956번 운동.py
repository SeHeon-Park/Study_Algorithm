# bfs

import sys, math
from collections import deque, defaultdict
input = sys.stdin.readline

v, e = map(int, input().split())
dic = defaultdict(dict)
for _ in range(e):
    a, b, c = map(int, input().split())
    dic[a][b] = c

ans = math.inf
flag = 0
Q = deque()

for i in range(1, v+1):
    Q.append((i, 0))
    dist = [-math.inf for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    ans_temp = math.inf
    while Q:
        cur, d = Q.popleft()
        if visited[cur] and cur == i:
            ans_temp = min(ans_temp, d)
            flag = 1
            continue
        for s, di in dic[cur].items():
            if visited[s] and dist[s]>di+d:
                dist[s] = di+d
                Q.append((s, di+d))
            if not visited[s]:
                visited[s] = 1
                dist[s] = di+d
                Q.append((s, di+d))
    if visited[i]:
        ans = min(ans, ans_temp)

if not flag:
    print(-1)
else:
    print(ans)


# 플로이드 워셜

import sys, math
input = sys.stdin.readline

v, e = map(int, input().split())
M = [[math.inf for _ in range(v)] for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    M[a-1][b-1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            M[i][j] = min(M[i][j], M[i][k]+M[k][j])

ans = math.inf
for i in range(v):
    ans = min(ans, M[i][i])

if ans == math.inf:
    print(-1)
else:
    print(ans)

