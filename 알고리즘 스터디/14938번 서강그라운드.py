# bfs(다익스트라, 152ms)

import sys, math
from collections import deque, defaultdict
input = sys.stdin.readline

dic = defaultdict(dict)

n, m, r = map(int, input().split())
t = [int(x) for x in input().split()]
for i in range(r):
    a, b, l = map(int, input().split())
    dic[a-1][b-1] = l
    dic[b-1][a-1] = l

Q = deque()
ans = 0
for i in range(n):
    Q.append((i, 0))
    visited = [0 for _ in range(n)]
    dist = [math.inf for _ in range(n)]
    visited[i] = 1
    cnt = t[i]
    while Q:
        cur, l = Q.popleft()
        for s, le in dic[cur].items():
            if l + le > m:
                continue
            if visited[s] and dist[s] > l+le:
                dist[s] = l+le
                Q.append((s, l+le))
            if not visited[s]:
                dist[s] = l + le
                visited[s] = 1
                cnt += t[s]
                Q.append((s, l+le))
    ans = max(ans, cnt)
print(ans)


# 플로이드 워셜 (176ms)

import sys, math
input = sys.stdin.readline


n, m, r = map(int, input().split())
t = [int(x) for x in input().split()]
M = [[math.inf for _ in range(n)] for _ in range(n)]

for i in range(r):
    a, b, l = map(int, input().split())
    M[a-1][b-1] = l
    M[b-1][a-1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            M[i][j] = min(M[i][j], M[i][k]+M[k][j])

ans = 0
for i in range(n):
    cnt = t[i]
    for j in range(n):
        if i == j:
            continue
        if M[i][j] <= m:
            cnt += t[j]
    ans = max(ans, cnt)
print(ans)
