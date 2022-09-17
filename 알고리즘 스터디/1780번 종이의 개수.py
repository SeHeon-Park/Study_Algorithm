import sys
input = sys.stdin.readline

def recursive(u, v, k):
    if k == 1:
        dic[M[u][v]] = dic[M[u][v]] + 1
        return

    s = M[u][v]
    flag = 0
    for i in range(u, u+k):
        for j in range(v, v+k):
            if M[i][j] != s:
                flag = 1
                break
    if not flag:
        dic[s] = dic[s] + 1
        return

    t = k//3
    for i in range(3):
        for j in range(3):
            recursive(u+i*t, v+j*t, k//3)
    return

n = int(input())
M = []
dic = {}
dic[-1], dic[0], dic[1] = 0, 0, 0

for _ in range(n):
    M.append(list(map(int, input().split())))

recursive(0,0,n)
for ans in dic.values():
    print(ans)