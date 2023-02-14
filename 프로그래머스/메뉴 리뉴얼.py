from collections import defaultdict, deque


def solution(orders, course):
    answer = []

    def dfs(idx, s):
        if len(s) == l:
            dic[s] += 1
            return
        for i in range(idx, len(r)):
            dfs(i+1, s+r[i])

    for c in course:
        dic = defaultdict(int)
        for o in orders:
            if c > len(o):
                continue
            r = sorted(o)
            l = c
            dfs(0, "")
        key, var = deque(), 2
        for k, v in dic.items():
            if v > var:
                if key:
                    key.clear()
                key.append(k)
                var = v
            elif v == var:
                key.append(k)

        for q in key:
            answer.append(q)

    return sorted(answer)
