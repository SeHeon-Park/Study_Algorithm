import math

def find_max(b, t):
    temp = 6
    while True:
        if b!=temp and t!=temp:
            return temp
        temp-=1

n = int(input())
D = []
dic={0:5, 1:3, 2:4, 5:0, 3:1, 4:2}
for _ in range(n):
    D.append(list(map(int, input().split())))

ans = -math.inf
for i in range(6):
    b = D[0][i]
    t = D[0][dic[i]]
    cnt = find_max(b, t)
    for j in range(1, n):
        idx = D[j].index(t)
        b = D[j][idx]
        t = D[j][dic[idx]]
        cnt += find_max(b, t)
    ans = max(ans, cnt)

print(ans)