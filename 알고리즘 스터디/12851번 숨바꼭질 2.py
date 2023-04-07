import sys
from collections import deque
input = sys.stdin.readline

x, y = map(int, input().split())
visited = [int(1e9) for _ in range(100001)]
ans_time = int(1e9)
ans_count = 1

Q = deque()
Q.append((x, 0))
visited[x] = 0

while Q:
    cur, time = Q.popleft()
    if cur < 0 or cur > 100000 or time > ans_time:
        continue
    if cur == y:
        if ans_time == time:
            ans_count += 1
        elif ans_time > time:
            ans_time = time
            ans_count = 1
        continue
    elif cur > y:
        time += (cur - y)
        if ans_time == time:
            ans_count += 1
        elif ans_time > time:
            ans_time = time
            ans_count = 1
        continue
    if visited[cur] < time:
        continue
    visited[cur] = time
    Q.append((2*cur, time+1))
    Q.append((cur+1, time+1))
    Q.append((cur-1, time+1))

print(ans_time)
print(ans_count)