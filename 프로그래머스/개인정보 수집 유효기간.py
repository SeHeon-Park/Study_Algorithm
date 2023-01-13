import re

def expired(s, T):
    info = re.split("[ ]", s)
    v = info[1]  # 약관
    time = T[v]
    start = re.split("[.]", info[0])
    y, m, d = int(start[0]), int(start[1]), int(start[2])
    ## 달
    m += time
    if m > 12:
        r = m // 12
        m = m % 12
        if m == 0:
            m = 12
            y -= 1
        y += r
    ## 일
    d -= 1
    if d == 0:
        m -= 1
        if m == 0:
            m = 12
            y -= 1
        d = 28
    return [y, m, d]

def check(t, c):
    if t[0] < c[0]:
        return False
    elif t[0] > c[0]:
        return True
    if t[1] < c[1]:
        return False
    elif t[1] > c[1]:
        return True

    if t[2] < c[2]:
        return False
    elif t[2] > c[2]:
        return True
    return False


def solution(today, terms, privacies):
    answer = []
    target = []
    for t in re.split("[.]", today):
        target.append(int(t))

    T = {}
    for t in terms:
        info = re.split("[ ]", t)
        T[info[0]] = int(info[1])

    idx = 1
    for p in privacies:
        if check(target, expired(p, T)):
            answer.append(idx)
        idx += 1

    return answer
