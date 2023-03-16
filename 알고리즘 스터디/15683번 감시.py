import sys
input = sys.stdin.readline

def shot(x, y, d):
    dir_x = dx[d]
    dir_y = dy[d]
    T = []
    cnt = 0
    while True:
        x += dir_x
        y += dir_y
        if x<0 or x>m-1 or y<0 or y>n-1 or M[y][x] == 6:
            break
        if M[y][x] or M[y][x] == -1:
            continue
        M[y][x] = -1
        T.append((x, y))
        cnt += 1
    return T, cnt

def remove(T):
    for t in T:
        for x, y in t:
            M[y][x] = 0

def dfs(count, idx):
    global ans
    for i in range(idx, len(info)):
        x, y = info[i]
        c = M[y][x]-1
        for d in range(len(dir[c])):
            temp, I = 0, []
            for t in dir[c][d]:
                T, cnt = shot(x, y, t)
                I.append(T)
                temp += cnt
            dfs(count + temp, idx+1)
            remove(I)
    ans = max(ans, count)
    return


n, m = map(int, input().split())
M = []
info = []
ans = 0

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 방향

dir = [
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [1, 3], [1, 2], [0, 2]],
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
]

for _ in range(n):
    M.append(list(map(int, input().split())))

temp = 0
answer = 0
for i in range(n):
    for j in range(m):
        if M[i][j] == 6:
            temp += 1
            continue
        if M[i][j] > 0:
            temp += 1
            if M[i][j] != 5:
                info.append((j, i))
            else:
                for zx, zy in zip(dx, dy):
                    x, y = j, i
                    while True:
                        x += zx
                        y += zy
                        if x < 0 or x > m - 1 or y < 0 or y > n - 1 or M[y][x] == 6:
                            break
                        if M[y][x] or M[y][x] == -1:
                            continue
                        M[y][x] = -1
                        answer += 1

dfs(0, 0)
print(m*n - (answer+ans+temp))
