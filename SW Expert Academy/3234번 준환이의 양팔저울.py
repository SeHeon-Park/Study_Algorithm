import math

def dfs(lw, rw, w):
    global cnt
    if w == n:
        cnt += 1
        return
    if lw > weight//2:
        cnt += ((2**(n-w)) * math.factorial(n-w))
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(lw + W[i], rw, w + 1)
        if rw+W[i] <= lw:
            dfs(lw, rw + W[i], w + 1)
        visited[i] = 0
    return

T = int(input())
for t in range(T):
    n = int(input())
    W = list(map(int, input().split()))
    weight = sum(W)
    visited = [0 for _ in range(n)]
    cnt = 0
    dfs(0, 0, 0)
    print("#{} {}".format(t+1, cnt))