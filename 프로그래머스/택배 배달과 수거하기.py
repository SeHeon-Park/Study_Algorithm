from heapq import heappush, heappop


def solution(cap, n, deliveries, pickups):
    answer = 0
    D, P = [], []
    for i in range(n):
        if deliveries[i]:
            heappush(D, (-(i+1), deliveries[i]))
        if pickups[i]:
            heappush(P, (-(i+1), pickups[i]))

    while True:
        if not D and not P:
            break

        w = cap
        temp = []
        flag = 0
        l3, l4 = 0, 0
        while True:
            if w == 0 or not D:
                break
            l, cnt = heappop(D)
            if not flag:
                l3 = l
            flag = 1
            if w >= cnt:
                w -= cnt
            else:
                temp.append((l, cnt-w))
                break

        for l, cnt in temp:
            heappush(D, (l, cnt))

        w = cap
        flag = 0
        temp = []
        while True:
            if w == 0 or not P:
                break
            l, cnt = heappop(P)
            if not flag:
                l4 = l
            flag = 1
            if w >= cnt:
                w -= cnt
            else:
                temp.append((l, cnt-w))
                break

        for l, cnt in temp:
            heappush(P, (l, cnt))

        if -l3 > -l4:
            answer += (l3*2)
        else:
            answer += (l4*2)

    return -answer