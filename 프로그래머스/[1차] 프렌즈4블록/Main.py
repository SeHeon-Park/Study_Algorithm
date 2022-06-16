from collections import deque


def pop_item(board, visited):
    boardV2 = [[] for _ in range(len(board))]
    visitedV2 = [[] for _ in range(len(board))]
    cnt = 0
    for i in range(len(board)):
        deq1 = deque(board[i])
        deq2 = deque(visited[i])
        while deq1:
            m = deq2.popleft()
            if m == 0:
                deq1.popleft()
                cnt += 1
            else:
                visitedV2[i].append(m)
                boardV2[i].append(deq1.popleft())
    return boardV2, visitedV2, cnt


def visit(visited, x_l, y_l):
    x = [1, 0, 1]
    y = [0, 1, 1]
    visited[y_l][x_l] = 0
    x_temp = x_l
    y_temp = y_l
    for i in zip(x, y):
        x_l = x_temp + i[0]
        y_l = y_temp + i[1]
        visited[y_l][x_l] = 0
    return visited


def select(board, x_l, y_l, visited):
    x = [1, 0, 1]
    y = [0, 1, 1]
    x_temp = x_l
    y_temp = y_l
    flag = 0
    for i in zip(x, y):
        x_l = x_temp + i[0]
        y_l = y_temp + i[1]
        if board[y_temp][x_temp] != board[y_l][x_l]:
            flag = 1
            break
    if flag == 0:
        visited = visit(visited, x_temp, y_temp)
    return visited


def solution(m, n, board):
    boardV2 = []
    answer = 0
    cnt = 0
    visited = [[1 for _ in range(m)] for _ in range(n)]
    for r in range(n):
        part = []
        for h in range(m - 1, -1, -1):
            part.append(board[h][r])
        boardV2.append(part)
    while True:
        for j in range(n - 1):
            m = min(len(boardV2[j]), len(boardV2[j+1]))
            for i in range(m-1):
                visited = select(boardV2, i, j, visited)
        boardV2, visited, cnt = pop_item(boardV2, visited)
        if cnt == 0:
            break
        answer += cnt
    return answer