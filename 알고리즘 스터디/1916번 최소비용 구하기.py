# bfs (248ms)
import sys, math
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
m = int(input())
dic = defaultdict(dict)
Q = deque()

for _ in range(m):
    a, b, w = map(int, input().split())
    if b-1 in dic[a-1].keys():
        dic[a-1][b-1] = min(dic[a-1][b-1], w)
    else:
        dic[a-1][b-1] = w

s, e = map(int, input().split())
Q.append((s-1, 0))
visited = [0] * n
dist = [math.inf] * n

while Q:
    cur, w = Q.popleft()
    if cur == e-1 and visited[cur]:
        continue
    for c, we in dic[cur].items():
        if visited[c] and dist[c] > w+we:
            dist[c] = w+we
            Q.append((c, w+we))
        if not visited[c]:
            visited[c] = 1
            dist[c] = w + we
            Q.append((c, w + we))
print(dist[e-1])



# 다익스트라 (280ms)
import sys, math
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())
dic = defaultdict(dict)
H = []
visited = [0 for _ in range(n)]
dist = [math.inf for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())
    if b-1 in dic[a-1].keys():
        dic[a-1][b-1] = min(dic[a-1][b-1], w)
    else:
        dic[a-1][b-1] = w

s, e = map(int, input().split())
dist[s-1] = 0
H.append(0)
cur = s-1

while H:
    p = heappop(H)
    # 주변 노드 update
    for c, w in dic[cur].items():
        if dist[c] > dist[cur]+w:
            dist[c] = dist[cur]+w
            heappush(H, dist[c])
    visited[cur] = 1
    m = math.inf
    # 가장 작은 노드 찾기
    for i in range(n):
        if not visited[i] and m > dist[i]:
            cur = i
            m = dist[i]

