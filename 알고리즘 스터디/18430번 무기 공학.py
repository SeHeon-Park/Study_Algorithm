import sys
input = sys.stdin.readline

def dfs(y, value):
    global ans
    for i in range(y, n):
        for j in range(m):
            if visited[i][j]:
                continue
            if i-1>=0 and j+1<=m-1 and not visited[i-1][j] and not visited[i][j+1]:
                visited[i][j] = 1
                visited[i-1][j] = 1
                visited[i][j+1] = 1
                dfs(i, value + M[i][j]*2 + M[i-1][j] + M[i][j+1])
                visited[i][j] = 0
                visited[i-1][j] = 0
                visited[i][j+1] = 0
            if i-1>=0 and j-1>=0 and not visited[i-1][j] and not visited[i][j-1]:
                visited[i][j] = 1
                visited[i-1][j] = 1
                visited[i][j-1] = 1
                dfs(i,value + M[i][j]*2 + M[i-1][j] + M[i][j-1])
                visited[i][j] = 0
                visited[i-1][j] = 0
                visited[i][j-1] = 0
            if i+1<=n-1 and j+1<=m-1 and not visited[i+1][j] and not visited[i][j+1]:
                visited[i][j] = 1
                visited[i+1][j] = 1
                visited[i][j+1] = 1
                dfs(i, value + M[i][j]*2 + M[i+1][j] + M[i][j+1])
                visited[i][j] = 0
                visited[i+1][j] = 0
                visited[i][j+1] = 0
            if i+1<=n-1 and j-1>=0 and not visited[i+1][j] and not visited[i][j-1]:
                visited[i][j] = 1
                visited[i+1][j] = 1
                visited[i][j-1] = 1
                dfs(i, value + M[i][j]*2 + M[i + 1][j] + M[i][j - 1])
                visited[i][j] = 0
                visited[i+1][j] = 0
                visited[i][j-1] = 0
    ans = max(ans, value)



n, m = map(int, input().split())
M = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    M.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(m):
        if i-1 >= 0 and j+1 <= m-1:
            visited[i][j] = 1
            visited[i-1][j] = 1
            visited[i][j + 1] = 1
            dfs(i, M[i][j]*2 + M[i-1][j] + M[i][j+1])
            visited[i][j] = 0
            visited[i-1][j] = 0
            visited[i][j+1] = 0
        if i-1 >= 0 and j-1 >= 0:
            visited[i][j] = 1
            visited[i-1][j] = 1
            visited[i][j-1] = 1
            dfs(i, M[i][j]*2 + M[i-1][j] + M[i][j-1])
            visited[i][j] = 0
            visited[i-1][j] = 0
            visited[i][j-1] = 0
        if i+1 <= n-1 and j+1 <= m-1:
            visited[i][j] = 1
            visited[i+1][j] = 1
            visited[i][j+1] = 1
            dfs(i, M[i][j]*2 + M[i+1][j] + M[i][j+1])
            visited[i][j] = 0
            visited[i+1][j] = 0
            visited[i][j+1] = 0
        if i+1 <= n-1 and j-1 >= 0:
            visited[i][j] = 1
            visited[i+1][j] = 1
            visited[i][j-1] = 1
            dfs(i, M[i][j]*2 + M[i+1][j] + M[i][j-1])
            visited[i][j] = 0
            visited[i+1][j] = 0
            visited[i][j-1] = 0
print(ans)

