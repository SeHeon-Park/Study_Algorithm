from collections import deque

def location(x, y, dir):
    x += dx[dir]
    if x < 0:
        x = c-1
    elif x > c-1:
        x = 0
    y += dy[dir]
    if y < 0:
        y = r-1
    elif y > r-1:
        y = 0
    return x, y

T = int(input())
for t in range(T):
    r, c = map(int, input().split())
    G = []
    M = 0
    Q = deque()
    for _ in range(r):
        G.append(list(map(str, input())))
    for i in range(r):
        for j in range(c):
            if 48 <= ord(G[i][j]) <= 57:
                G[i][j] = int(G[i][j])

    # 오, 아, 왼, 위
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    Q.append((0, 0, 0, 0))
    S = set()
    dic = {">":0, "v":1, "<":2, "^":3}
    flag = 0
    while Q:
        x, y, dir, m = Q.popleft()
        if G[y][x] == "@":
            flag = 1
            break
        if isinstance((G[y][x]), int):
            m = G[y][x]
        else:
            if G[y][x] == "?":
                for i in range(4):
                    dir = i
                    if (x, y, m, dir) in S:
                        continue
                    S.add((x, y, m, dir))
                    qx, qy = location(x, y, dir)
                    Q.append((qx, qy, dir, m))
                continue
            if G[y][x] == ">" or G[y][x] == "v" or G[y][x] == "<" or G[y][x] == "^":
                dir = dic[G[y][x]]
            elif G[y][x] == "+":
                m += 1
                if m > 15:
                    m = 0
            elif G[y][x] == "-":
                m -= 1
                if m < 0:
                    m = 15
            elif G[y][x] == "_":
                if m == 0:
                    dir = 0
                else:
                    dir = 2
            elif G[y][x] == "|":
                if m == 0:
                    dir = 1
                else:
                    dir = 3
        if (x, y, m, dir) in S:
            continue
        S.add((x, y, m, dir))
        x, y = location(x, y, dir)
        Q.append((x, y, dir, m))
    if flag:
        print("#{} YES".format(t+1))
    else:
        print("#{} NO".format(t+1))