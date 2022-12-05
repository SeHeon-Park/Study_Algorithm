import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(cur, depth):
    node[depth].append(cur)
    for c in down[cur]:
        dfs(c, depth+1)

n = int(input())
up = defaultdict(dict)
down = defaultdict(list)
for _ in range(n-1):
    u, v, w = map(int, input().split())
    up[v][u] = w
    down[u].append(v)

node = defaultdict(list)
ans = [[0] for _ in range(n+1)]
dfs(1, 0)
depth = max(node.keys())

for d in range(depth, 0, -1):
    for v in node[d]:
        for p, w in up[v].items():
            ans[p].append(max(ans[v])+w)
answer = 0
for a in ans:
    if len(a) > 2:
        a.sort()
        answer = max(answer, a[-1]+a[-2])

b = sorted(ans[1])[-1]
print(max(answer, b))
