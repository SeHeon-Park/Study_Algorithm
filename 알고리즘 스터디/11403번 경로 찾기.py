## 내 풀이(dfs) 304ms

from collections import defaultdict

def recursive(cur, path):
    if path and cur == j:
        for p in path[:-1]:
            M[i][p] = 1
        M[i][j] = 1
        return
    for d in dic[cur]:
        if not visited[d]:
            visited[d] = 1
            recursive(d, path + [d])
    return

n = int(input())
M = []
dic = defaultdict(list)
for _ in range(n):
    M.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if M[i][j] == 1:
            dic[i].append(j)


for i in range(n):
    for j in range(n):
        visited = [0 for _ in range(n)]
        if M[i][j] == 1:
            continue
        if not dic[i]:
            continue
        recursive(i, [])

for m in M:
    print(*m)

## 플로이드–워셜 알고리즘 160ms
n = int(input())
M = []
for _ in range(n):
    M.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if M[i][k] and M[k][j]:
                M[i][j] = 1

for m in M:
    print(*m)
