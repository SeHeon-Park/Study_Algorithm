from collections import deque

for t in range(10):
    n, s = map(str, input().split())
    n = int(n)
    s = list(map(str, s))
    Q1 = deque(s[1:])
    Q2 = deque(s[0])
    while Q1:
        if Q2 and Q2[-1] == Q1[0]:
            Q1.popleft()
            Q2.pop()
        else:
            Q2.append(Q1.popleft())
    ans = ''.join(Q2)
    print("#{} {}".format(t+1, ans))


