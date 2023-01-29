import math, re
from collections import defaultdict

def get_time(i, o):
    i_t = re.split(":", i)
    o_t = re.split(":", o)
    return (int(o_t[0])-int(i_t[0]))*60 + (int(o_t[1])-int(i_t[1]))

def solution(fees, records):
    ans = []
    C = {}
    T = defaultdict(int)
    for r in records:
        c = re.split(" ", r)
        c[1] = int(c[1])
        if c[2] == "IN":
            C[c[1]] = c[0]
        else:
            T[c[1]] = T[c[1]] + get_time(C[c[1]], c[0])
            del C[c[1]]
    if C:
        for c, t in C.items():
            T[c] = T[c] + get_time(t, "23:59")
    for c, t in T.items():
        if t <= fees[0]:
            ans.append([c, fees[1]])
        else:
            ans.append([c, fees[1]+(math.ceil((t-fees[0])/fees[2]))*fees[3]])
    ans.sort(key=lambda x:x[0])
    answer = []
    for a in ans:
        answer.append(a[1])
    return answer

