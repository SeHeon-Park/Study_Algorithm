import sys

def dot(A, B):
    ans = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ans[i][j] += A[i][k] * B[k][j]
    for i in range(N):
        for j in range(N):
            ans[i][j] %= 1000
    return ans


def recursion(A, B):
    if B == 1: return A
    t = recursion(A, B//2)
    if B % 2 == 1:
        return dot(dot(t, t), A)
    else:
        return dot(t, t)


N, B = map(int, input().split())
board = []
for i in range(N):
    L = list(map(int, sys.stdin.readline().split()))
    board.append(L)

for i in range(N):
    for j in range(N):
        board[i][j] %= 1000

answer = recursion(board, B)

for i in range(N):
    for j in range(N):
        print(answer[i][j], end=" ")
    print()



