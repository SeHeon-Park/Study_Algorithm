import sys

def solution(c1, c2, root):
    while c1 != root:
        visit[c1] = 1
        c1 = dic[c1]

    while c2 != root:
        if visit[c2] == 1:
            return c2
        c2 = dic[c2]
    return root

n = int(sys.stdin.readline())
for i in range(n):
    dic = {}
    t = int(sys.stdin.readline())
    visit = [0 for _ in range(t+1)]
    check = [0 for _ in range(t+1)]
    check[0] = 1
    for j in range(t-1):
        u, v = map(int, sys.stdin.readline().split())
        dic[v] = u
        check[v] = 1
    root = check.index(0)
    visit[root] = 1
    c1, c2 = map(int, sys.stdin.readline().split())
    print(solution(c1, c2, root))