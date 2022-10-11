import sys
from collections import deque

input = sys.stdin.readline


def move(start, target, number):
    if number == 0:
        if start > a-target:
            return start-a+target, a
        else:
            return 0, target+start
    elif number == 1:
        if start > b-target:
            return start-b+target, b
        else:
            return 0, target+start
    elif number == 2:
        if start > c-target:
            return start-c+target, c
        else:
            return 0, target+start


a, b, c = map(int, input().split())
ans = set()
S = set()
Q = deque()
Q.append((0, 0, c))

while Q:
    M = Q.popleft()
    if (M[0], M[1], M[2]) in S:
        continue
    if M[0] == 0:
        ans.add(M[2])
    S.add((M[0], M[1], M[2]))

    for i in range(3):
        if M[i] == 0:
            continue
        if i == 0:
            s, t = move(M[0], M[1], 1)
            Q.append((s, t, M[2]))
            s, t = move(M[0], M[2], 2)
            Q.append((s, M[1], t))
        elif i == 1:
            s, t = move(M[1], M[0], 0)
            Q.append((t, s, M[2]))
            s, t = move(M[1], M[2], 2)
            Q.append((M[0], s, t))
        elif i == 2:
            s, t = move(M[2], M[0], 0)
            Q.append((t, M[1], s))
            s, t = move(M[2], M[1], 1)
            Q.append((M[0], t, s))

for a in sorted(ans):
    print(a, end=" ")

