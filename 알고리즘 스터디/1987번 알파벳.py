import sys
input = sys.stdin.readline

def dfs(qx, qy, cur):
    global ans
    for zx, zy in zip(dx, dy):
        x = zx + qx
        y = zy + qy
        if x<0 or x>m-1 or y<0 or y>n-1 or visited[y][x] or A[ord(M[y][x])-65]:
            continue
        if cur in C[y][x]:
            continue
        visited[y][x] = 1
        A[ord(M[y][x])-65] = 1
        C[y][x].add(cur)
        dfs(x, y, cur+M[y][x])
        visited[y][x] = 0
        A[ord(M[y][x])-65] = 0
    if ans < len(cur):
        ans = len(cur)

n, m = map(int, input().split())
M = []
visited = [[0 for _ in range(m)] for _ in range(n)]
C = [[set() for _ in range(m)] for _ in range(n)]
S = set()
A = [0 for _ in range(26)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    M.append(list(map(str, input()[:-1])))

visited[0][0] = 1
A[ord(M[0][0])-65] = 1
ans = 1
dfs(0, 0, M[0][0])

print(ans)
