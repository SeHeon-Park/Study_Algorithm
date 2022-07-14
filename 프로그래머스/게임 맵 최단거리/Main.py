import math
from collections import deque

def solution(maps):
    visit = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    Q = deque([(0, 0, 1)]) # x, y, cnt
    ans = math.inf
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    while Q:
        x, y, cnt = Q.popleft()
        if x == len(maps[0])-1 and y == len(maps)-1:
            ans = min(cnt, ans)
            continue
        for sx, sy in zip(dx, dy):
            x += sx
            y += sy
            if 0<=x<len(maps[0]) and 0<=y<len(maps) and visit[y][x]==0 and maps[y][x]==1:
                visit[y][x] = 1
                Q.append((x, y, cnt+1))
            x -= sx
            y -= sy
    if ans == math.inf:
        return -1
    return ans


주의!
- dfs를 이용하면 효율성 통과x
- bfs를 이용해서 해야됨(queue이용)
