import sys, math
from collections import defaultdict
input = sys.stdin.readline

def cal(s, e):
    x1, y1 = dic[s]
    x2, y2 = dic[e]
    return math.sqrt(abs((x1-x2)**2+(y1-y2)**2))

def parent(a):
    if a != P[a]:
        P[a] = parent(P[a])
    return P[a]

def union(a, b):
    a = parent(a)
    b = parent(b)
    if a == b:
        return False
    if a < b:
        P[b] = a
    else:
        P[a] = b
    return True


n, m = map(int, input().split())
dic = defaultdict(tuple)
info = []
P = [int(x) for x in range(n+1)]

for i in range(n):
    x, y = map(int, input().split())
    dic[i+1] = (x, y)

for i in range(1, n):
    for j in range(i+1, n+1):
        info.append([i, j, cal(i, j)])

for _ in range(m):
    s, e = map(int, input().split())
    union(s, e)

info.sort(key=lambda x:x[2])

ans = 0
for i in info:
    if P[i[0]] != P[i[1]]:
        if union(i[0], i[1]):
            ans += i[2]

print(f"{ans:.2f}")



