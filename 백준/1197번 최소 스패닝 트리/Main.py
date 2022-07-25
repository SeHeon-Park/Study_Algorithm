import sys

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    parent[a] = b
    return True

v, e = map(int, input().split())
M = []
for i in range(e):
    M.append([int(x) for x in sys.stdin.readline().split()])

M.sort(key=lambda x:x[2])
parent = [-1 for i in range(v+1)]

ans = 0
for m in M:
    if union(m[0], m[1]):
        ans += m[2]

print(ans)