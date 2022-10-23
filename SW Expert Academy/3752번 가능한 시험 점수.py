T = int(input())

for t in range(T):
    n = int(input())
    M = [int(x) for x in input().split()]
    S = set()
    A = set()
    S.add(0)
    A.add(0)
    for m in M:
        temp = []
        for s in S:
            if m not in S:
                A.add(m)
                temp.append(m)
            if m + s not in S:
                A.add(m + s)
                temp.append(m + s)
        for a in temp:
            S.add(a)
    print("#{} {}".format(t + 1, len(A)))