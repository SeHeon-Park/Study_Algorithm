import sys
from collections import defaultdict
input = sys.stdin.readline

def parent(a):
    if a != P[a]:
        P[a] = parent(P[a])
    return P[a]

def union(a, b):
    P[a] = parent(a)
    P[b] = parent(b)
    if a<b:
        P[b] = a
    else:
        P[a] = b

n = int(input())
m = int(input())

P = [int(x) for x in range(n+1)]
dic = defaultdict(list)

for _ in range(m):
    ef, p, q = map(str, input().split())
    p = int(p)
    q = int(q)
    if ef == "F":
        union(p, q)
    else:
        dic[p].append(q)
        dic[q].append(p)


for i in range(1, n+1):
    for v in dic[i]:
        for u in dic[v]:
            if i != u:
                union(i, u)

S = set()
for i in range(1, n+1):
    S.add(parent(i))

print(len(S))

