import sys
from collections import deque, defaultdict
# input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    I = [int(x) for x in input().split()]
    M = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, n):
            M[I[i]][I[j]] = 1
    m = int(input())
    info = []
    Q = deque()
    for _ in range(m):
        u, v = map(int, input().split())
        if M[u][v]:
            M[v][u] = 1
            M[u][v] = 0
        else:
            M[v][u] = 0
            M[u][v] = 1

    dic = defaultdict(list)
    C = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if M[i][j] == 1:
                dic[j].append(i)
                C[i] += 1

    for i in range(1, n+1):
        if C[i] == 0:
            Q.append(i)

    if not Q:
        print("IMPOSSIBLE")
        continue

    ans = []
    flag = 0
    while Q:
        if len(Q) > 1:
            flag = 1
            break
        u = Q.popleft()
        ans.append(u)
        for v in dic[u]:
            C[v] -= 1
            if not C[v]:
                Q.append(v)


    if flag:
        print("?")
    if len(ans) != n:
        print("IMPOSSIBLE")
    else:
        ans.reverse()
        print(*ans)

