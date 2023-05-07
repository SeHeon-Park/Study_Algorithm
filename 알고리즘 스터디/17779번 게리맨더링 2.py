import sys, math
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
P = []
su = 0
for _ in range(n):
    info = list(map(int, input().split()))
    su += sum(info)
    P.append(info)

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
ans = math.inf

for x in range(1, n):
    for y in range(1, n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if x<x+d1+d2<=n and 1<=y-d1<y<y+d2<=n:
                    s = su
                    dic = [0 for _ in range(6)]
                    S = set()
                    S.add((x, y))

                    # 1, 2
                    x_temp1, y_temp1 = x, y
                    x_temp2, y_temp2 = x, y
                    cnt = 0
                    while True:
                        if cnt == d1:
                            dic[5] += P[x_temp1-1][y_temp1-1]
                            S.add((x_temp1, y_temp1))
                            break
                        dic[5] += P[x_temp1-1][y_temp1-1]
                        S.add((x_temp1, y_temp1))
                        x_temp1 += 1
                        y_temp1 -= 1
                        cnt += 1
                    cnt = 0
                    while True:
                        if cnt == d2:
                            dic[5] += P[x_temp2-1][y_temp2-1]
                            S.add((x_temp2, y_temp2))
                            break
                        dic[5] += P[x_temp2-1][y_temp2-1]
                        S.add((x_temp2, y_temp2))
                        x_temp2 += 1
                        y_temp2 += 1
                        cnt += 1

                    # 3, 4
                    cnt = 0
                    while True:
                        if cnt == d2:
                            dic[5] += P[x_temp1-1][y_temp1-1]
                            S.add((x_temp1, y_temp1))
                            break
                        dic[5] += P[x_temp1-1][y_temp1-1]
                        S.add((x_temp1, y_temp1))
                        x_temp1 += 1
                        y_temp1 += 1
                        cnt += 1
                    cnt = 0
                    while True:
                        if cnt == d1:
                            dic[5] += P[x_temp2-1][y_temp2-1]
                            S.add((x_temp2, y_temp2))
                            break
                        dic[5] += P[x_temp2-1][y_temp2-1]
                        S.add((x_temp2, y_temp2))
                        x_temp2 += 1
                        y_temp2 -= 1
                        cnt += 1

                    Q = deque()
                    # 선거구 4
                    r, c = n, n
                    S.add((r, c))
                    Q.append((r, c))
                    dic[4] += P[r-1][c-1]
                    while Q:
                        qr, qc = Q.popleft()
                        for zr, zc in zip(dx, dy):
                            r = qr+zr
                            c = qc+zc
                            if x+d2<r<=n and y-d1+d2<=c<=n:
                                if (r, c) in S: continue
                                S.add((r, c))
                                dic[4] += P[r-1][c-1]
                                Q.append((r, c))

                    # 선거수 3
                    r, c = n, 1
                    S.add((r, c))
                    Q.append((r, c))
                    dic[3] += P[r - 1][c - 1]
                    while Q:
                        qr, qc = Q.popleft()
                        for zr, zc in zip(dx, dy):
                            r = qr + zr
                            c = qc + zc
                            if x+d1<=r<= n and 1<=c<y-d1+d2:
                                if (r, c) in S: continue
                                S.add((r, c))
                                dic[3] += P[r - 1][c - 1]
                                Q.append((r, c))

                    r, c = 1, n
                    S.add((r, c))
                    Q.append((r, c))
                    dic[2] += P[r - 1][c - 1]
                    while Q:
                        qr, qc = Q.popleft()
                        for zr, zc in zip(dx, dy):
                            r = qr + zr
                            c = qc + zc
                            if 1 <= r <= x+d2 and y< c <= n:
                                if (r, c) in S: continue
                                S.add((r, c))
                                dic[2] += P[r - 1][c - 1]
                                Q.append((r, c))

                    # 선거구 1
                    r, c = 1, 1
                    S.add((r, c))
                    Q.append((r, c))
                    dic[1] += P[r - 1][c - 1]
                    while Q:
                        qr, qc = Q.popleft()
                        for zr, zc in zip(dx, dy):
                            r = qr + zr
                            c = qc + zc
                            if 1 <= r < x + d1 and 1 <= c <= y:
                                if (r, c) in S: continue
                                S.add((r, c))
                                dic[1] += P[r - 1][c - 1]
                                Q.append((r, c))

                    s -= sum(dic)
                    dic[5] += s
                    dic.sort()
                    ans = min(ans, dic[-1]-dic[1])
print(ans)