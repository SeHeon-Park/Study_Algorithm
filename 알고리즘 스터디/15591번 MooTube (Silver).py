# dfs

from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**5)

def dfs(k, cur, mi):
    global ans
    if k <= mi:
        ans += 1
    for p, r in dic[cur].items():
        if visited[p]:
            continue
        visited[p] = 1
        dfs(k, p, min(mi, r))
        visited[p] = 0
    return

N, Q = map(int, input().split())
dic = defaultdict(dict)
visited = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    dic[p][q] = r
    dic[q][p] = r

for _ in range(Q):
    k, m = map(int, input().split())
    ans = -1
    visited[m] = 1
    dfs(k, m, math.inf)
    visited[m] = 0
    print(ans)


# bfs

from collections import defaultdict, deque
import math

N, Q = map(int, input().split())
dic = defaultdict(dict)
dq = deque()

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    dic[p][q] = r
    dic[q][p] = r

for _ in range(Q):
    k, m = map(int, input().split())
    visited = [0 for _ in range(N + 1)]
    ans = -1
    visited[m] = 1
    dq.append((m, math.inf))
    while dq:
        cur, mi = dq.popleft()
        if k <= mi:
            ans += 1
        for p, r in dic[cur].items():
            if visited[p]:
                continue
            visited[p] = 1
            dq.append((p, min(mi, r)))
    print(ans)


