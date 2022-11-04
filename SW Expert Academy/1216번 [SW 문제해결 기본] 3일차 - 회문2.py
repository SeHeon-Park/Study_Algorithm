from itertools import combinations
import math

def check_w(l, r, idx):
    while l<r:
        if M[idx][l] != M[idx][r]:
            return False
        l+=1
        r-=1
    return True

def check_h(l, r, idx):
    while l<r:
        if M[l][idx] != M[r][idx]:
            return False
        l+=1
        r-=1
    return True

for t in range(10):
    n = int(input())
    M = []
    ans = -math.inf
    for _ in range(100):
        M.append(list(map(str, input())))

    N = [int(x+1) for x in range(99)]
    L = list(combinations(N, 2))
    L.sort(key=lambda x:x[1]-x[0], reverse=True)
    for i in range(100):
        for l, r in L:
            if check_w(l, r, i):
                if ans != -math.inf and ans >= r-l+1:
                    break
                ans = r-l+1
            if check_h(l, r, i):
                if ans != -math.inf and ans >= r-l+1:
                    break
                ans = r-l+1
    if ans != -math.inf:
        print("#{} {}".format(t+1, ans))
    else:
        print("#{} {}".format(t+1, 1))
