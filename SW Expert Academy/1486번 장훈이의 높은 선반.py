from collections import deque
import math

T = int(input())
for t in range(T):
    n, b = map(int, input().split())
    T = [int(x) for x in input().split()]
    Q = deque()
    Q.append((0, 1))
    Q.append((T[0], 1))
    ans = math.inf
    while Q:
        w, idx = Q.popleft()
        if w >= ans:
            continue
        if idx > n-1:
            if w >= b:
                ans = min(ans, w)
            continue
        Q.append((w, idx+1))
        Q.append((w+T[idx], idx+1))
    print("#{} {}".format(t+1, ans-b))