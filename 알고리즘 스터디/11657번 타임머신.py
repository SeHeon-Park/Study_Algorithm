import sys
input = sys.stdin.readline
INF = int(1e9)

def check_cycle(s):
    dist[s] = 0
    for i in range(n):
        for s, e, t in edges:
            print(s, e, dist)
            # if dist[s] != INF  ->  0노드에서 아직 방문하지 않은 노드이므로 update 할 필요 없음
            if dist[s] != INF and dist[e] > dist[s]+t:
                dist[e] = dist[s]+t
                if i == n-1:
                    return False
    return True

n, m = map(int, input().split())
edges = []
dist = [INF for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a-1, b-1, c))

if check_cycle(0):
    for d in range(1, n):
        if dist[d] == INF:
            print(-1)
        else:
            print(dist[d])
else:
    print(-1)