# 다익스트라 (640ms)
import sys, math
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
s = int(input())
dic = defaultdict(dict)
H = []
visited = [0] * n
dist = [math.inf] * n

for _ in range(m):
    a, b, w = map(int, input().split())
    if b-1 in dic[a-1].keys():
        dic[a-1][b-1] = min(dic[a-1][b-1], w)
    else:
        dic[a-1][b-1] = w

dist[s-1] = 0
H.append((0, s-1))

while H:
    weight, cur = heappop(H)
    if visited[cur]:
        continue
    # 주변 노드 update
    for c, w in dic[cur].items():
        if dist[c] > dist[cur]+w:
            dist[c] = dist[cur]+w
            heappush(H, (dist[c], c))
    visited[cur] = 1

for d in dist:
    if d == math.inf:
        print("INF")
    else:
        print(d)

# bfs (시간 초과)
import sys, math
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
s = int(input())
dic = defaultdict(dict)
Q = deque()

for _ in range(m):
    a, b, w = map(int, input().split())
    if b-1 in dic[a-1].keys():
        dic[a-1][b-1] = min(dic[a-1][b-1], w)
    else:
        dic[a-1][b-1] = w

Q.append((s-1, 0))
visited = [0] * n
dist = [math.inf] * n
dist[s-1] = 0

while Q:
    cur, w = Q.popleft()
    for c, we in dic[cur].items():
        if visited[c] and dist[c] > w+we:
            dist[c] = w+we
            Q.append((c, w+we))
        if not visited[c]:
            visited[c] = 1
            dist[c] = w + we
            Q.append((c, w + we))
for d in dist:
    if d == math.inf:
        print("INF")
    else:
        print(d)