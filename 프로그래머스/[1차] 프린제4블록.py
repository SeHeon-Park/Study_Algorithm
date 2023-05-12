def delete(C, M):
    m, n = len(C), len(C[0])
    cnt = 0
    for i in range(m-1):
        for j in range(n-1):
            if M[i][j] == 0: continue
            temp = M[i][j]
            if M[i][j+1] == temp and M[i+1][j] == temp and M[i+1][j+1] == temp:
                C[i][j+1] = 1
                C[i+1][j] = 1
                C[i+1][j+1] = 1
                C[i][j] = 1
    for i in range(m):
        for j in range(n):
            if C[i][j] == 1:
                M[i][j] = 0
                cnt += 1
    return cnt, M

def gravity(M):
    m, n = len(M), len(M[0])
    for x in range(n):
        for y in range(m-2, -1, -1):
            if M[y][x] == 0: continue
            prev, next = y, y+1
            while True:
                if next > m-1 or M[next][x] != 0:
                    break
                M[prev][x], M[next][x] = 0, M[prev][x]
                prev += 1
                next += 1
    return M

def solution(m, n, board):
    ans = 0
    M = []
    for b in board:
        B = list(b)
        M.append(B)
    while True:
        C = [[0 for _ in range(n)] for _ in range(m)]
        cnt, M = delete(C, M)
        if not cnt: break
        ans += cnt
        M = gravity(M)
    return ans

solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])