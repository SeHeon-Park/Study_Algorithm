import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(k):
    global ans
    for a in dic[k]:
        if visited[a] == 1:
            continue
        ans += 1
        visited[a] = 1
        dfs(a)
    return

n = int(input())
l = int(input())
dic = defaultdict(list)
visited = [0 for _ in range(n+1)]
visited[1] = 1
ans = 0

for _ in range(l):
    u, v = map(int, input().split())
    dic[u].append(v)
    dic[v].append(u)

dfs(1)

print(ans)