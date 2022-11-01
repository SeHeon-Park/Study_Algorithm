def dfs(x, y):
    global tf
    if tf or x==11 and y==11:
        tf = True
        return
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for zx, zy in zip(dx, dy):
        fx = x + zx
        fy = y + zy
        if fx<0 or fx>15 or fy<0 or fy>15 or visited[fy][fx] or M[fx][fy]==1:
            continue
        visited[fy][fx] = 1
        dfs(fx, fy)
        visited[fy][fx] = 0
    return


for t in range(10):
    int(input())
    M = []
    tf = False
    for _ in range(16):
        M.append(list(map(int, input())))
    visited = [[0 for _ in range(16)] for _ in range(16)]
    dfs(1, 1)
    if tf:
        print("#{} {}".format(t+1, 1))
    else:
        print("#{} {}".format(t+1, 0))