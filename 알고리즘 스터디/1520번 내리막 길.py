import sys
input = sys.stdin.readline

def dfs(qx, qy):
    global ans
    if qx == m-1 and qy == n-1:
        dp[n-1][m-1] += 1
        return dp[n-1][m-1]
    temp = 0
    for zx, zy in zip(dx, dy):
        x = qx+zx
        y = qy+zy
        if x<0 or x>m-1 or y<0 or y>n-1 or M[qy][qx]-M[y][x]<=0:
            continue
        if visited[y][x]:
            temp += dp[y][x]
            continue
        visited[y][x] = 1
        temp += dfs(x, y)
    dp[qy][qx] += temp
    return temp

n, m = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
M = []
for _ in range(n):
    M.append(list(map(int, input().split())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dfs(0, 0)
print(dp[0][0])