# 플로이드-워셜 (656ms)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
M = []
for _ in range(n):
    M.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            M[i][j] = min(M[i][j], M[i][k]+M[k][j])


for _ in range(m):
    a, b, c = map(int, input().split())
    if M[a-1][b-1] > c:
        print("Stay here")
    else:
        print("Enjoy other party")



# bfs (1304ms)

import sys, math
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
M = []
S = [[] for _ in range(n)]
Q = deque()

for _ in range(n):
    M.append(list(map(int, input().split())))

for s in range(n):
    T = [math.inf for _ in range(n)]
    Q.append((s, 0))
    while Q:
        cur, time = Q.popleft()
        for i in range(n):
            t = M[cur][i]
            if i == cur:
                continue
            if time + t > T[i]:
                continue
            T[i] = time+M[cur][i]
            Q.append((i, time+t))
    for t in T:
        S[s].append(t)

for _ in range(m):
    a, b, c = map(int, input().split())
    if S[a-1][b-1] > c:
        print("Stay here")
    else:
        print("Enjoy other party")
