# 벨만 포드 (288ms)
# ※ 모든 간선의 비용이 양수일 때는 다익스트라, 음수 간선이 포함되어 있으면 벨만-포드

import sys
input = sys.stdin.readline

# math.inf + (양수) = math.inf
# int(1e9) + (양수) > int(1e9)
# --> 기억해라 박세헌
INF = int(1e9)

def bellman_ford(s):
    distance = [INF] * (n+1)
    distance[s] = 0
    for i in range(n):
        for s, e, t in edges:
            if distance[e] > distance[s] + t:
                distance[e] = distance[s] + t
                # 마지막 돌렸는데 또 갱신 되면 음의 사이클 존재한다는 것
                if i == n-1:
                    return True
    return False

T = int(input())
for _ in range(T):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    # 음의 사이클만 구하면 되기 때문에 시작점 하나만 판별
    if bellman_ford(1):
        print("YES")
    else:
        print("NO")



# bfs (시간 초과)

import sys, math
from collections import defaultdict, deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m, w = map(int, input().split())
    dic = defaultdict(dict)
    Q = deque()
    for _ in range(m):
        s, e, t = map(int, input().split())
        if e-1 in dic[s-1].keys():
            dic[s-1][e-1] = [min(dic[s-1][e-1][0], t)]
            dic[e-1][s-1] = [min(dic[e-1][s-1][0], t)]
        else:
            dic[s-1][e-1] = [t]
            dic[e-1][s-1] = [t]
    for _ in range(w):
        s, e, t = map(int, input().split())
        if e-1 in dic[s-1].keys():
            dic[s-1][e-1].append(-t)
        else:
            dic[s-1][e-1] = [-t]
    for i in range(n):
        Q.append((i, 0))
        visited = [0 for _ in range(n)]
        time = [math.inf for _ in range(n)]
        flag = 0
        while Q:
            cur, t = Q.popleft()
            if visited[cur] and cur == i and t<0:
                flag = 1
                break
            for s, ti in dic[cur].items():
                if len(ti) > 1:
                    if visited[s] and t+ti[1] < time[s]:
                        time[s] = t+ti[1]
                        Q.append((s, t+ti[1]))
                    if not visited[s]:
                        visited[s] = 1
                        time[s] = t+ti[1]
                        Q.append((s, t+ti[1]))
                else:
                    if visited[s] and t+ti[0] < time[s]:
                        time[s] = t+ti[0]
                        Q.append((s, t+ti[0]))
                    if not visited[s]:
                        visited[s] = 1
                        time[s] = t+ti[0]
                        Q.append((s, t+ti[0]))
        if flag:
            break
    if flag:
        print("YES")
    else:
        print("NO")



# 플로이드 워셜 (시간 초과)

import sys, math
input = sys.stdin.readline

def floyd_warshal():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if M[i][j] > M[i][k] + M[k][j]:
                    M[i][j] = M[i][k] + M[k][j]
                if i == j and M[i][i] < 0:
                    return True
    return False

T = int(input())
for _ in range(T):
    n, m, w = map(int, input().split())
    M = [[math.inf for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        if M[s-1][e-1] > t:
            M[s-1][e-1] = t
            M[e-1][s-1] = t
    for _ in range(w):
        s, e, t = map(int, input().split())
        M[s-1][e-1] = -t
    if floyd_warshal():
        print("YES")
    else:
        print("NO")