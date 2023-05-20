from bisect import bisect_left

def solution(n, t, m, timetable):
    answer = -1
    dic = {}
    c = 540
    bus, table = [], []
    for i in range(n):
        bus.append(c)
        dic[c] = []
        c += t

    for tt in timetable:
        tt = tt.split(":")
        hour = int(tt[0])
        minute = int(tt[1])
        table.append(hour*60 + minute)

    table.sort()
    for ta in table:
        idx = bisect_left(bus, ta)
        if idx > len(bus)-1:
            continue
        p = bus[idx]
        while True:
            if p not in dic.keys():
                break
            if len(dic[p]) == m:
                p += t
            else:
                dic[p].append(ta)
                break

    c -= t
    if len(dic[c]) < m:
        answer = c
    else:
        flag = 0
        while True:
            if flag or c not in dic.keys():
                break
            L = dic[c]
            late = L[-1]
            for i in range(m-2, -1, -1):
                if late != L[i]:
                    answer = L[i]
                    flag = 1
                    break
            if late-1 not in dic.keys():
                answer = late-1
                break
            c -= t

    if answer == -1:
        answer = dic[540][0]-1

    hour = str(answer // 60)
    minute = str(answer % 60)
    if len(hour) == 1:
        hour = "0"+hour
    if len(minute) == 1:
        minute = "0"+minute
    ans = hour + ":" + minute

    return ans
