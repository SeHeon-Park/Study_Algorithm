from collections import defaultdict
import math

def dfs(s, depth):
    global ans
    ans = max(ans, depth)
    for e in dic[s]:
        if visited[e]:
            continue
        visited[e] = 1
        dfs(e, depth+1)
        visited[e] = 0
    return

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    visited = [0 for _ in range(N+1)]
    dic = defaultdict(set)
    ans = -math.inf
    if M:
        for m in range(M):
            x, y = map(int, input().split())
            dic[x].add(y)
            dic[y].add(x)
        for s in dic.keys():
            visited[s] = 1
            dfs(s, 1)
            visited[s] = 0
        print("#{} {}".format(t + 1, ans))
    else:
        print("#{} {}".format(t+1, 1))