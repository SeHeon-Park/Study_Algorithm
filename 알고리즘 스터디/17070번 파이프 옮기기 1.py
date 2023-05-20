import sys
input = sys.stdin.readline


def dfs(x1, y1, x2, y2):
    global ans
    if x2 == n-1 and y2 == n-1:
        ans += 1
        return
    # 가로
    if x2-x1 == 1 and y2-y1 == 0:
        if x2+1 <= n-1 and M[y2][x2+1] != 1 and (x2, y2, x2+1, y2) not in S:
            dfs(x2, y2, x2+1, y2)
        if x2+1 <= n-1 and y2+1 <= n-1 and M[y2+1][x2+1] != 1 and M[y2][x2+1] != 1 and M[y2+1][x2] != 1:
            dfs(x2, y2, x2+1, y2+1)

    # 세로
    if x2-x1 == 0 and y2-y1 == 1:
        if y2+1 <= n-1 and M[y2+1][x2] != 1:
            dfs(x2, y2, x2, y2+1)
        if x2+1 <= n-1 and y2+1 <= n-1 and M[y2+1][x2+1] != 1 and M[y2][x2+1] != 1 and M[y2+1][x2] != 1:
            dfs(x2, y2, x2+1, y2+1)

    # 대각선
    if x2-x1 == 1 and y2-y1 == 1:
        if x2+1 <= n-1 and M[y2][x2+1] != 1:
            dfs(x2, y2, x2+1, y2)
        if y2+1 <= n-1 and M[y2+1][x2] != 1:
            dfs(x2, y2, x2, y2+1)
        if x2+1 <= n-1 and y2+1 <= n-1 and M[y2+1][x2+1] != 1 and M[y2][x2+1] != 1 and M[y2+1][x2] != 1:
            dfs(x2, y2, x2+1, y2+1)


n = int(input())
M = []
for _ in range(n):
    M.append(list(map(int, input().split())))

ans = 0
dfs(0, 0, 1, 0)
print(ans)