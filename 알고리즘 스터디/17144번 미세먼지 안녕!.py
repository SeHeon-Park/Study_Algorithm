import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
M = []
D = []
for i in range(r):
    m = list(map(int, input().split()))
    if -1 in m:
        D.append(i)
    M.append(m)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(t):
    # 확산
    T = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if M[i][j] > 0:
                cnt = 0
                value = M[i][j] // 5
                for zx, zy in zip(dx, dy):
                    x = j + zx
                    y = i + zy
                    if x<0 or x>c-1 or y<0 or y>r-1 or M[y][x] == -1:
                        continue
                    cnt += 1
                    T[y][x] += value
                M[i][j] = M[i][j] - (value*cnt)
    for i in range(r):
        for j in range(c):
            M[i][j] = M[i][j] + T[i][j]

    # 위 순환
    # 우, 상, 좌, 하
    tx = [1, 0, -1, 0]
    ty = [0, -1, 0, 1]
    x, y = 1, D[0]
    dir = 0
    S = set()
    while True:
        v = M[y][x]
        x += tx[dir]
        y += ty[dir]
        if x<0 or x>c-1 or y<0 or y>r-1:
            x -= tx[dir]
            y -= ty[dir]
            dir += 1
            continue
        if M[y][x] == -1:
            break
        M[y-ty[dir]][x-tx[dir]] = 0
        S.add((y, x, v))
    for s in S:
        M[s[0]][s[1]] = s[2]

    # 아래 순환
    # 우, 하, 좌, 상
    bx = [1, 0, -1, 0]
    by = [0, 1, 0, -1]
    x, y = 1, D[1]
    dir = 0
    S = set()
    while True:
        v = M[y][x]
        x += bx[dir]
        y += by[dir]
        if x<0 or x>c-1 or y<0 or y>r-1:
            x -= bx[dir]
            y -= by[dir]
            dir += 1
            continue
        if M[y][x] == -1:
            break
        M[y-by[dir]][x-bx[dir]] = 0
        S.add((y, x, v))
    for s in S:
        M[s[0]][s[1]] = s[2]

ans = 2
for m in M:
    ans += sum(m)
print(ans)
