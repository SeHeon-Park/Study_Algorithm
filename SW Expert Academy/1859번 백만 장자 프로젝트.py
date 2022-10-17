from collections import Counter
 
def get_cnt(A, i):
    c = 0
    for a in A:
        c += (i - a)
    return c
 
t = int(input())
for c in range(t):
    n = int(input())
    M = [int(x) for x in input().split()]
    A = sorted(M)
    C = Counter(A)
    ma = A[-1]
    ans, cnt = [], 0
    for m in M:
        if m != ma:
            ans.append(m)
            C[m] = C[m] - 1
        else:
            cnt += get_cnt(ans, m)
            ans = []
            ma = A.pop()
            C[ma] = C[ma] - 1
            while True:
                if not A:
                    break
                ma = A[-1]
                if C[ma] == 0:
                    A.pop()
                    continue
                else:
                    break
            if not A:
                break
 
    print("#{} {}".format(c+1, cnt))