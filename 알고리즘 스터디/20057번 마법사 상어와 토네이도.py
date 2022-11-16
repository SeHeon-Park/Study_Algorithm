import sys
input = sys.stdin.readline

def in_range(x, y):
    return x>=0 and x<=n-1 and y>=0 and y<=n-1

def move(x, y, dir):
    global ans
    # 5
    s = 0
    ux = x + dx[dir]*2
    uy = y + dy[dir]*2
    v = (M[y][x] * 5) // 100
    s += v
    if in_range(ux, uy):
        M[uy][ux] += v
    else:
        ans += v

    # 7
    ld, rd = dir+1, dir-1
    if ld > 3:
        ld = 0
    if rd < 0:
        rd = 3
    lx, rx = x, x
    ly, ry = y, y
    lx += dx[ld]
    ly += dy[ld]
    v = (M[y][x] * 7) // 100
    s += (v * 2)
    if in_range(lx, ly):
        M[ly][lx] += v
    else:
        ans += v
    rx += dx[rd]
    ry += dy[rd]
    if in_range(rx, ry):
        M[ry][rx] += v
    else:
        ans += v

    # 10, 2, 1
    c = [10, 2, 1]
    direction_l = [dir]
    direction_r = [dir]
    if dir+1 > 3:
        direction_l.append(0)
    else:
        direction_l.append(dir+1)
    if dir-1 < 0:
        direction_r.append(3)
    else:
        direction_r.append(dir-1)
    if dir+2 > 3:
        direction_l.append(dir-2)
        direction_r.append(dir-2)
    else:
        direction_l.append(dir+2)
        direction_r.append(dir+2)

    for i in range(3):
        ax = lx + dx[direction_l[i]]
        ay = ly + dy[direction_l[i]]
        v = (M[y][x] * c[i]) // 100
        s += (v * 2)
        if in_range(ax, ay):
            M[ay][ax] += v
        else:
            ans += v
        bx = rx + dx[direction_r[i]]
        by = ry + dy[direction_r[i]]
        if in_range(bx, by):
            M[by][bx] += v
        else:
            ans += v

    # a
    ux = x + dx[dir]
    uy = y + dy[dir]
    v = M[y][x] - s
    if v > 0:
        if in_range(ux, uy):
            M[uy][ux] += v
        else:
            ans += v

n = int(input())
M = []
for _ in range(n):
    M.append(list(map(int, input().split())))

curr = (n//2, n//2)
# 좌, 아, 우, 위
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir, cnt, m, ans, flag = 0, 0, 1, 0, 0

while True:
    for _ in range(m):
        curr = (curr[0]+dx[dir], curr[1]+dy[dir])
        move(curr[0], curr[1], dir)
        if curr[0] == 0 and curr[1] == 0:
            flag = 1
            break
        M[curr[1]][curr[0]] = 0
    if flag:
        break
    cnt += 1
    dir += 1
    if dir > 3:
        dir = 0
    if cnt == 2:
        m += 1
        cnt = 0

print(ans)