import sys, math
input = sys.stdin.readline

n, m, h = map(int, input().split())
ans = math.inf
A = [[0 for _ in range(n+1)] for _ in range(h+1)]
B = set()

for i in range(1, h + 1):
    for j in range(1, n):
        B.add((i, j))

for _ in range(m):
    a, b = map(int, input().split())
    A[a][b] = 1
    B.remove((a, b))
    if (a, b + 1) in B:
        B.remove((a, b + 1))
    if (a, b - 1) in B:
        B.remove((a, b - 1))

B = list(B)

def check():
    for i in range(1, n+1):
        location = i
        height = 1
        while height < h + 1:
            if A[height][location - 1]:
                location -= 1
            elif A[height][location]:
                location += 1
            height += 1
        if location != i:
            return False
    return True

def dfs(A, cnt, idx):
    global ans
    if ans <= cnt or cnt > 3:
        return
    if check():
        ans = min(ans, cnt)
        return
    for b in range(idx, len(B)):
        A[B[b][0]][B[b][1]] = 1
        dfs(A, cnt+1, b+1)
        A[B[b][0]][B[b][1]] = 0
    return


dfs(A, 0, 0)
if ans != math.inf:
    print(ans)
else:
    print(-1)

