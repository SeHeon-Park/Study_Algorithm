import sys
input = sys.stdin.readline

def find_height(o, k):
    if o == -1:
        return 0
    s, p = 0, k
    height = 1
    while True:
        if s <= o <= s+p-1:
            return height
        s = s+p
        p = p*k
        height += 1


n, k, q = map(int, input().split())

for _ in range(q):
    u, v = map(int, input().split())
    if k == 1:
        print(abs(u-v))
        continue
    u -= 2
    v -= 2

    height1 = find_height(u, k)
    height2 = find_height(v, k)
    cnt1, cnt2 = 0, 0

    while True:
        if u == v:
            # print("공통 조상 :", u+2)
            break
        if height1 > height2:
            u = u//k-1
            cnt1 += 1
            height1 -= 1
        elif height1 < height2:
            v = v//k-1
            cnt2 += 1
            height2 -= 1
        else:
            while u != v:
                u = u//k-1
                v = v//k-1
                cnt1 += 1
                cnt2 += 1

    print(cnt1+cnt2)
