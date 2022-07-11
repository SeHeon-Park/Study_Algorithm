import math

def check(queries, board):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    counter = [queries[2]-queries[0], queries[3]-queries[1], queries[2]-queries[0], queries[3]-queries[1]]
    for i in range(len(queries)):
        queries[i] -= 1
    x = queries[1]
    y = queries[0]
    temp = board[y][x]
    m = temp
    for zx, zy, c in zip(dx, dy, counter):
        for j in range(c):
            board[y][x] = board[y+zy][x+zx]
            m = min(m, board[y+zy][x+zx])
            y += zy
            x += zx
    board[y][x+1] = temp
    return board, m
    
def solution(rows, columns, queries):
    board = []
    answer = []
    f = columns
    s = 1
    for i in range(rows):
        board.append([j for j in range(s, f + 1)])
        s += columns
        f += columns
    for q in queries:
        board, m = check(q, board)
        answer.append(m)
    return answer