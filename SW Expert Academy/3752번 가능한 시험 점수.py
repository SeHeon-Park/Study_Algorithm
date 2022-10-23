T = int(input())


def recursion(idx, temp):
    A.add(temp)
    if idx == n:
        return
    print(A)
    for a in A:
        if M[idx] not in A:
            recursion(idx+1, M[idx])
        if a+M[idx] not in A:
            recursion(idx+1, a+M[idx])
    return


for t in range(T):
    n = int(input())
    M = [int(x) for x in input().split()]
    A = set()
    A.add(0)
    recursion(0, 0)
    print("#{} {}".format(t + 1, len(A)))