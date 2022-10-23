def dfs(s, qx, qy):
    if len(s) == 7:
        P.add(s)
        return
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for zx, zy in zip(dx, dy):
        x = qx + zx
        y = qy + zy
        if x < 0 or x > 3 or y < 0 or y > 3:
            continue
        dfs(s+M[y][x], x, y)
    return
 
T = int(input())
 
for t in range(T):
    M = []
    for _ in range(4):
        M.append(list(str(x) for x in input().split()))
    P = set()
    for i in range(4):
        for j in range(4):
            dfs(M[j][i], i, j)
    print("#{} {}".format(t+1, len(P)))