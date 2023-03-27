import sys
from collections import deque
input = sys.stdin.readline

def dfs(cur):
    global cnt
    if cnt == len(cur):
        T = tuple(sorted(cur))
        if T in S:
            return
        S.add(T)
        g.append(cur)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(cur + [i])
        visited[i] = 0

def bfs(group):
    Q = deque()
    Q.append(group[0])
    visited[group[0]] = 1
    sum, c = people[group[0]], 1
    while Q:
        v = Q.popleft()
        for o in M[v]:
            if visited[o] or o not in group:
                continue
            visited[o] = 1
            c += 1
            sum += people[o]
            Q.append(o)
    if c != len(group):
        return False, -1
    return True, sum


n = int(input())
people = [int(x) for x in input().split()]
S = sum(people)
P = [int(i) for i in range(n)]
V = [int(i) for i in range(n)]
M = [[] for _ in range(n)]

for i in range(n):
    info = list(map(int, input().split()))
    for j in range(1, len(info)):
        M[i].append(info[j]-1)

ans = 1000

S = set()
for cnt in range(1, n//2+1):
    for cur in range(n):
        g = []
        visited = [0 for _ in range(n)]
        visited[cur] = 1
        dfs([cur])
        for group1 in g:
            visited = [0 for _ in range(n)]
            tf, sum1 = bfs(group1)
            if not tf:
                continue
            visited= [0 for _ in range(n)]
            group2 = [v for v in V if v not in group1]
            if tuple(sorted(group2)) in S:
                continue
            tf, sum2 = bfs(group2)
            if not tf:
                continue
            ans = min(ans, abs(sum1-sum2))

if ans == 1000:
    print(-1)
else:
    print(ans)