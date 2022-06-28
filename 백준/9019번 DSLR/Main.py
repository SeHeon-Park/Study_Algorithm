from collections import deque

t = int(input())
for i in range(t):
    A, B = input().split()
    for i in range(4-len(A)):
        A = '0' + A
    q = deque()
    q.append((A, ''))
    visit = [False] * 10000
    while q:
        num1, path = q.popleft()
        print(num1)
        visit[int(num1)] = True
        if int(num1) == int(B):
            print(path)
            break

        # D
        num2 = 2 * int(num1)
        if num2 > 9999:
            num2 = num2 % 10000
        if not visit[num2]:
            num2 = str(num2)
            for i in range(4 - len(num2)):
                num2 = '0' + num2
            q.append((num2, path+'D'))
            visit[int(num2)] = True

        # S
        if num2 == 0:
            num2 = 9999
        else:
            num2 = int(num1) - 1
        if not visit[num2]:
            num2 = str(num2)
            for i in range(4 - len(num2)):
                num2 = '0' + num2
            q.append((num2, path + 'S'))
            visit[int(num2)] = True

        # L
        num2 = ''
        for i in range(1, len(num1)):
            num2 += num1[i]
        num2 = num2 + num1[0]
        if not visit[int(num2)]:
            q.append((num2, path + 'L'))
            visit[int(num2)] = True

        # R
        num2 = ''
        num2 += num1[-1]
        for i in range(len(num1)-1):
            num2 += num1[i]
        if not visit[int(num2)]:
            q.append((num2, path + 'R'))
            visit[int(num2)] = True

