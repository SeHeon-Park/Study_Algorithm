from collections import deque, defaultdict


def solution(game_board, table):
    n = len(table)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    piece = defaultdict(dict)

    def make_rectangle():
        max_x, min_x, max_y, min_y = 0, 100, 0, 100
        for p in P:
            max_x = max(max_x, p[1])
            min_x = min(min_x, p[1])
            max_y = max(max_y, p[0])
            min_y = min(min_y, p[0])

        for p in P:
            if min_x < 0:
                p[1] += (-min_x)
            if min_y < 0:
                p[0] += (-min_y)

        M = [[0 for _ in range(max_x - min_x+1)] for _ in range(max_y - min_y+1)]

        for p in P:
            M[p[0]][p[1]] = 1

        return M

    def rotation(M):
        len_x = len(M[0])
        len_y = len(M)
        T = []
        for x in range(len_x):
            temp = []
            for y in range(len_y-1, -1, -1):
                temp.append(M[y][x])
            T.append(temp)
        return T

    num = 0
    Q = deque()
    for i in range(n):
        for j in range(n):
            if not table[i][j] or visited[i][j]:
                continue
            P, cnt = [], 1
            visited[i][j] = 1
            P.append([0, 0])
            Q.append((i, j))
            while Q:
                qy, qx = Q.popleft()
                for zx, zy in zip(dx, dy):
                    x = zx + qx
                    y = zy + qy
                    if x < 0 or x > n - 1 or y < 0 or y > n - 1 or not table[y][x] or visited[y][x]:
                        continue
                    visited[y][x] = 1
                    cnt += 1
                    P.append([y - i, x - j])
                    Q.append((y, x))
            piece[cnt][num]=make_rectangle()
            num += 1
    check = [0 for _ in range(num)]

    ans = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    Q = deque()
    for i in range(n):
        for j in range(n):
            if game_board[i][j] or visited[i][j]:
                continue
            P, cnt = [], 1
            visited[i][j] = 1
            P.append([0, 0])
            Q.append((i, j))
            while Q:
                qy, qx = Q.popleft()
                for zx, zy in zip(dx, dy):
                    x = zx + qx
                    y = zy + qy
                    if x < 0 or x > n - 1 or y < 0 or y > n - 1 or game_board[y][x] or visited[y][x]:
                        continue
                    visited[y][x] = 1
                    cnt += 1
                    P.append([y - i, x - j])
                    Q.append((y, x))
            O = make_rectangle()
            flag = 0
            for num, p in piece[cnt].items():
                if flag:
                    break
                if check[num]: continue
                for _ in range(4):
                    if p == O:
                        ans += cnt
                        flag = 1
                        check[num] = 1
                        break
                    O = rotation(O)

    return ans

