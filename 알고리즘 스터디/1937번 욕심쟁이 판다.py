import sys
input = sys.stdin.readline

def dfs(qx, qy):
    for zx, zy in zip(dx, dy):
        x = zx + qx
        y = zy + qy
        if x<0 or x>n-1 or y<0 or y>n-1 or M[qy][qx] >= M[y][x]:
            continue
        if visited[y][x]:
            dp[qy][qx] = max(dp[qy][qx], dp[y][x]+1)
            continue
        visited[y][x] = 1
        dp[qy][qx] = max(dfs(x, y)+1, dp[qy][qx])
    return dp[qy][qx]

n = int(input())
M = []
visited = [[0 for _ in range(n)] for _ in range(n)]
dp = [[1 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    M.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(j, i))

print(ans)