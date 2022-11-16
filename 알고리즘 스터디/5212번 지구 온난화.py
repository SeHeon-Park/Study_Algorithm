r, c = map(int, input().split())
M = []

for _ in range(r):
    M.append(list(map(str, input())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
S = set()
max_x = 0
min_x = c-1
max_y = 0
min_y = r-1

for i in range(r):
    for j in range(c):
        if M[i][j] == 'X':
            cnt = 0
            for zx, zy in zip(dx, dy):
                x = j + zx
                y = i + zy
                if x < 0 or x > c-1 or y < 0 or y > r-1:
                    cnt += 1
                    continue
                if M[y][x] == '.':
                    cnt += 1
            if cnt < 3:
                max_x = max(max_x, j)
                min_x = min(min_x, j)
                max_y = max(max_y, i)
                min_y = min(min_y, i)
                S.add((j, i))

y = max_y-min_y+1
x = max_x-min_x+1
for i in range(y):
    for j in range(x):
        if (j+min_x, i+min_y) in S:
            print('X', end='')
        else:
            print('.', end='')
    print()