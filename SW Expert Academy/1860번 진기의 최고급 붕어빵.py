from collections import defaultdict

T = int(input())
for t in range(1, T+1):
    n, m, k = map(int, input().split())
    N = list(map(int, input().split()))
    dic = defaultdict(int)
    for i in N:
        dic[i] += 1

    cnt, flag, s = 0, 0, m
    for i in range(max(N)+1):
        if i == s:
            cnt += k
            s += m
        if i in dic.keys():
            if dic[i] > cnt:
                flag = 1
                break
            else:
                cnt -= dic[i]
    if flag:
        print("#{0} Impossible".format(t))
    else:
        print("#{0} Possible".format(t))

