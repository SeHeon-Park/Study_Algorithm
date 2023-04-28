import sys

input = sys.stdin.readline


def up(M):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    temp = [m[:] for m in M]
    for x in range(n):
        for y in range(1, n):
            cur = temp[y][x]
            y_front = y - 1
            y_back = y
            while True:
                if y_front == -1:
                    break
                if temp[y_front][x] == 0:
                    temp[y_front][x], temp[y_back][x] = cur, 0
                    y_front -= 1
                    y_back -= 1
                    continue
                if temp[y_front][x] != cur:
                    break
                else:
                    if visited[y_front][x] == 0:
                        temp[y_front][x] *= 2
                        temp[y_back][x] = 0
                        visited[y_front][x] = 1
                    break
    return temp


def down(M):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    temp = [m[:] for m in M]
    for x in range(n):
        for y in range(n - 2, -1, -1):
            cur = temp[y][x]
            y_front = y + 1
            y_back = y
            while True:
                if y_front == n:
                    break
                if temp[y_front][x] == 0:
                    temp[y_front][x], temp[y_back][x] = cur, 0
                    y_front += 1
                    y_back += 1
                    continue
                if temp[y_front][x] != cur:
                    break
                else:
                    if visited[y_front][x] == 0:
                        temp[y_front][x] *= 2
                        temp[y_back][x] = 0
                        visited[y_front][x] = 1
                    break
    return temp


def left(M):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    temp = [m[:] for m in M]
    for y in range(n):
        for x in range(1, n):
            cur = temp[y][x]
            x_front = x - 1
            x_back = x
            while True:
                if x_front == -1:
                    break
                if temp[y][x_front] == 0:
                    temp[y][x_front], temp[y][x_back] = cur, 0
                    x_front -= 1
                    x_back -= 1
                    continue
                if temp[y][x_front] != cur:
                    break
                else:
                    if visited[y][x_front] == 0:
                        temp[y][x_front] *= 2
                        temp[y][x_back] = 0
                        visited[y][x_front] = 1
                    break
    return temp


def right(M):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    temp = [m[:] for m in M]
    for y in range(n):
        for x in range(n - 2, -1, -1):
            cur = temp[y][x]
            x_front = x + 1
            x_back = x
            while True:
                if x_front == n:
                    break
                if temp[y][x_front] == 0:
                    temp[y][x_front], temp[y][x_back] = cur, 0
                    x_front += 1
                    x_back += 1
                    continue
                if temp[y][x_front] != cur:
                    break
                else:
                    if visited[y][x_front] == 0:
                        temp[y][x_front] *= 2
                        temp[y][x_back] = 0
                        visited[y][x_front] = 1
                    break
    return temp


def dfs(cnt, M):
    global ans
    if cnt == 5:
        for m in M:
            ans = max(ans, max(m))
        return

    T = [m[:] for m in M]

    dfs(cnt + 1, up(M))
    M = [t[:] for t in T]

    dfs(cnt + 1, down(M))
    M = [t[:] for t in T]

    dfs(cnt + 1, left(M))
    M = [t[:] for t in T]

    dfs(cnt + 1, right(M))
    M = [t[:] for t in T]
    return


n = int(input())
M = []
for _ in range(n):
    M.append(list(map(int, input().split())))


ans = 0
dfs(0, M)
print(ans)