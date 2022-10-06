import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(fx, fy, point, r):
    global ans
    if point == cnt:
        ans.append(r)
        return
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for zx, zy in zip(dx, dy):
        flag = 0
        V = []
        x = fx
        y = fy
        while True:
            x += zx
            y += zy
            if 0<=x<=m-1 and 0<=y<=n-1 and M[y][x] == '.' and not visited[y][x]:
                V.append((x, y))
                visited[y][x] = 1
                point += 1
                flag = 1
            else:
                if flag:
                    dfs(x - zx, y - zy, point, r + 1)
                    for v in V:
                        visited[v[1]][v[0]] = 0
                        point -= 1
                break
    return

case = 0
while True:
    try:
        n, m = map(int, input().split())
        cnt = 0
        M, ans = [], []
        visited = [[0 for _ in range(m)] for _ in range(n)]
        case += 1

        for _ in range(n):
            p = list(map(str, input()))
            cnt += p.count('.')
            M.append(p)

        for i in range(n):
            for j in range(m):
                if M[i][j] == '*':
                    visited[i][j] = 1

        temp = copy.deepcopy(visited)
        for i in range(n):
            for j in range(m):
                if M[i][j] == '.':
                    visited[i][j] = 1
                    dfs(j, i, 1, 0)
                    visited=copy.deepcopy(temp)

        if ans:
            print("Case {}: {}".format(case, min(ans)))
        else:
            print("Case {}: {}".format(case, -1))
    except:
        break