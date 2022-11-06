from collections import deque


def check(px, py):
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, 1, -1, -1, 1]
    for zx, zy in zip(dx, dy):
        x = px + zx
        y = py + zy
        if x<0 or x>n-1 or y<0 or y>n-1:
            continue
        if M[y][x] == "*":
            return
    return True

T = int(input())

for t in range(T):
    n = int(input())
    cnt = 0
    M = []
    S = set()
    Q = deque()
    for i in range(n):
        M.append(list(map(str, input())))
    for i in range(n):
        for j in range(n):
            if M[i][j] == '.' and check(j, i):
                cnt += 1
                Q.append((j, i))
                while Q:
                    qx, qy = Q.popleft()
                    if not check(qx, qy):
                        continue
                    M[qy][qx] = 'c'
                    dx = [0, 1, 0, -1, 1, 1, -1, -1]
                    dy = [1, 0, -1, 0, 1, -1, -1, 1]
                    for zx, zy in zip(dx, dy):
                        x = qx + zx
                        y = qy + zy
                        if x < 0 or x > n - 1 or y < 0 or y > n - 1 or M[y][x] == 'c':
                            continue
                        if (x, y) in S:
                            S.remove((x, y))
                        M[y][x] = 'c'
                        Q.append((x, y))
            elif M[i][j] == '.' and not check(j, i):
                S.add((j, i))
    print("#{} {}".format(t+1, cnt + len(S)))