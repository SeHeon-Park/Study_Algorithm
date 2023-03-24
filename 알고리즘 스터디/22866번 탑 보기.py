import sys
input = sys.stdin.readline

n = int(input())
M = [int(x) for x in input().split()]
T = [[M[0], 0]]
ans = [[0, -1, 0] for _ in range(n)] # cnt, idx, 거리

# 왼쪽
for i in range(1, n):
    idx = len(T)-1
    while True:
        if not T:
            break
        if T[idx][0] > M[i]:
            ans[i][0] = len(T)
            ans[i][1] = T[idx][1]+1
            ans[i][2] = abs(i-T[idx][1])
            break
        if T[idx][0] <= M[i]:
            T.pop()
        idx -= 1
    T.append([M[i], i])


T = [[M[-1], len(M)-1]]

# 오른쪽
for i in range(n-2, -1, -1):
    idx = len(T)-1
    while True:
        if not T:
            break
        if T[idx][0] > M[i]:
            ans[i][0] = ans[i][0]+len(T)
            if ans[i][1] != -1 and ans[i][2] <= abs(i-T[idx][1]):
                break
            ans[i][1] = T[idx][1]+1
            ans[i][2] = abs(i-T[idx][1])
            break
        if T[idx][0] <= M[i]:
            T.pop()
        idx -= 1
    T.append([M[i], i])

for a in ans:
    if a[1] == -1:
        print(0)
    else:
        print(a[0], a[1])
