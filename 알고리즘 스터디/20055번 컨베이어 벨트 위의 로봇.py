import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = [[int(x), 0] for x in input().split()]

robot = []
cycle = 1
z = 0

while True:
    # 1
    idx = -1
    for r in range(len(robot)):
        robot[r] += 1
        if robot[r] == n-1:
            A[robot[r]][1] = 0
            idx = r
    A = [A[-1]] + A[:-1]
    if idx != -1:
        del robot[idx]
        if A[n-1][0] != 0:
            A[n-1] = [A[n-1][0], 0]

    # 2
    idx = -1
    for r in range(len(robot)):
        if robot[r] + 1 == n-1:
            if A[robot[r]+1][0] and not A[robot[r]+1][1]:
                idx = r
                A[robot[r]][1] = 0
                A[robot[r]+1][0] -= 1
                if A[robot[r]+1][0] == 0:
                    z += 1
        else:
            if A[robot[r]+1][0] and not A[robot[r]+1][1]:
                A[robot[r]][1] = 0
                robot[r] += 1
                A[robot[r]][0] -= 1
                A[robot[r]][1] = 1
                if A[robot[r]][0] == 0:
                    z += 1
    if idx != -1:
        del robot[idx]

    # 3
    if A[0][0] != 0 and not A[0][1]:
        A[0][0] -= 1
        A[0][1] = 1
        robot.append(0)
        if A[0][0] == 0:
            z += 1
    # 4
    if z >= k:
        break

    cycle += 1

print(cycle)
