import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
dic = {}
child = [[] for i in range(n+1)]
ans = []
deq = deque()

for i in range(n):
    dic[i+1] = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[b] += 1
    child[a].append(b)

for k in dic.keys():
    if dic[k] == 0:
        deq.append(k)


while deq:
    s = deq.popleft()
    ans.append(s)
    for c in child[s]:
        dic[c] -= 1
        if dic[c] == 0:
            deq.append(c)

for a in ans:
    print(a, end=" ")
