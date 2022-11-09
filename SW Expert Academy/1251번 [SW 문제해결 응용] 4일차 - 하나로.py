from itertools import combinations

# 재귀로 부모 찾으면서 update
def find_parent(P, a):
    if a != P[a]:
        P[a] = find_parent(P, P[a])
    return P[a]

# 각자 부모를 찾아 큰거에 작은거 삽입
def union_parent(P, a, b):
    a = find_parent(P, a)
    b = find_parent(P, b)
    if a > b:
        P[a] = b
    else:
        P[b] = a

def distance(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

T = int(input())
for t in range(T):
    n = int(input())
    I = [[0, 0, 0] for _ in range(n)]
    visited = [0 for _ in range(n)]
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    for i, XY in enumerate(zip(X, Y)):
        I[i][0] = XY[0]
        I[i][1] = XY[1]
        I[i][2] = i
    e = float(input())
    D = []
    for c in combinations(I, 2):
        D.append([c[0][2], c[1][2], distance(c[0], c[1])])
    D.sort(key=lambda x: x[2])
    P = [int(i) for i in range(n)]
    ans = 0
    for d in D:
        if find_parent(P, d[0]) != find_parent(P, d[1]):
            union_parent(P, d[0], d[1])
            ans += d[2]

    print("#{} {}".format(t+1, round(ans * e)))

