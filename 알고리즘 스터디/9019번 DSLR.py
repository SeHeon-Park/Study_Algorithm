from collections import deque

t = int(input())

for i in range(t):
    A, B = map(int, input().split())
    Q = deque()
    Q.append((A, ''))
    visit = [0 for _ in range(10000)]
    while Q:
        num1, path = Q.popleft()

        # D
        num2 = 2 * num1
        if num2 > 9999:
            num2 = num2 % 10000
        if num2 == B:
            print(path+'D')
            break
        if not visit[num2]:
            visit[num2] = 1
            Q.append((num2, path + 'D'))

        # S
        if num1 == 0:
            num2 = 9999
        else:
            num2 = num1 - 1
        if num2 == B:
            print(path+'S')
            break
        if not visit[num2]:
            visit[num2] = 1
            Q.append((num2, path + 'S'))

        # L
        num2 = (num1 % 1000) * 10 + num1 // 1000
        if num2 == B:
            print(path+'L')
            break
        if not visit[num2]:
            visit[num2] = 1
            Q.append((num2, path + 'L'))

        # R
        num2 = (num1 % 10) * 1000 + num1 // 10
        if num2 == B:
            print(path+'R')
            break
        if not visit[num2]:
            visit[num2] = 1
            Q.append((num2, path + 'R'))