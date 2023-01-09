import sys
input = sys.stdin.readline

n = int(input())
M = []
for i in range(n):
    M.append(list(map(int, input().split())))

dp1 = [0 for _ in range(3)]
dp2 = [0 for _ in range(3)]

for i in range(3):
    dp1[i] = M[0][i]
    dp2[i] = M[0][i]

for h in range(1, n):
    a1 = dp1[0]
    b1 = dp1[1]
    c1 = dp1[2]
    a2 = dp2[0]
    b2 = dp2[1]
    c2 = dp2[2]

    dp1[0] = (M[h][0] + min(a1, b1))
    dp1[1] = (M[h][1] + min(a1, b1, c1))
    dp1[2] = (M[h][2] + min(b1, c1))

    dp2[0] = (M[h][0] + max(a2, b2))
    dp2[1] = (M[h][1] + max(a2, b2, c2))
    dp2[2] = (M[h][2] + max(b2, c2))


print(max(dp2), min(dp1))

