import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

M = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    M[x-1][y-1] = 2
M[0][0] = 1
S = []
l = int(input())
for _ in range(l):
    x, d = map(str, input().split())
    x = int(x)
    S.append([x, d])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir_h = 0
dir_t = 0

idx = 0
time = 0
h = [0, 0]
t = [0, 0]
Q = deque()

while True:
    hx, hy = list(zip(dx, dy))[dir_h]
    tx, ty = list(zip(dx, dy))[dir_t]
    time += 1
    h[0] += hy
    h[1] += hx
    if h[0] < 0 or h[0] > n-1 or h[1] < 0 or h[1] > n-1 or M[h[0]][h[1]] == 1:
        break
    if M[h[0]][h[1]] == 2:
        M[h[0]][h[1]] = 1
    else:
        M[h[0]][h[1]] = 1
        M[t[0]][t[1]] = 0
        t[0] += ty
        t[1] += tx
        if Q and Q[0][:-1] == t:
            dir_t = Q.popleft()[2]
    if idx < l and time == S[idx][0]:
        if S[idx][1] == 'L':
            dir_h -= 1
            if dir_h < 0:
                dir_h = 3
        else:
            dir_h += 1
            if dir_h > 3:
                dir_h = 0
        idx += 1
        if h == t:
            dir_t = dir_h
            continue
        Q.append([h[0], h[1], dir_h])

print(time)