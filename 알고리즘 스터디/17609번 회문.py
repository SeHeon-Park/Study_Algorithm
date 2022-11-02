import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for t in range(T):
    s = input()[:-1]
    l, r = 0, len(s)-1
    Q = deque()
    Q.append((l, r, 0))
    ans = -1
    while Q:
        l, r, cnt = Q.popleft()
        if cnt == 2:
            continue
        if l >= r:
            if cnt:
                ans = 1
            else:
                ans = 0
            break
        if s[l] != s[r]:
            Q.append((l+1, r, cnt+1))
            Q.append((l, r-1, cnt+1))
            continue
        Q.append((l+1, r-1, cnt))

    if ans == -1:
        print(2)
    else:
        print(ans)
