from collections import defaultdict, deque

for k in range(10):
    t, l = map(int, input().split())
    S = set()
    dic = defaultdict(list)
    M = [int(x) for x in input().split()]
    Q = deque()
    for i in range(0, len(M)-1, 2):
        dic[M[i]].append(M[i+1])
    Q.append(0)
    flag = 0
    while Q:
        curr = Q.popleft()
        if curr == 99:
            flag = 1
            break
        for c in dic[curr]:
            if c in S:
                continue
            S.add(c)
            Q.append(c)
    if flag:
        print("#{} {}".format(t, 1))
    else:
        print("#{} {}".format(t, 0))