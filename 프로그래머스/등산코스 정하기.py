from collections import defaultdict
from heapq import heappush, heappop
import math


def solution(n, paths, gates, summits):
    ans =[]
    summits = set(summits)
    dic = defaultdict(dict)
    H = []
    for s, e, w in paths:
        dic[s][e] = w
        dic[e][s] = w
    dist = [math.inf for _ in range(n + 1)]
    for g in gates:
        H.append((g, 0))
    while H:
        cur, w = heappop(H)
        if cur in summits:
            ans.append([cur, w])
            continue
        if dist[cur] < w:
            continue
        for target, weight in dic[cur].items():
            temp = w
            if temp < weight:
                temp = weight
            if dist[target] > temp:
                dist[target] = temp
                heappush(H, (target, temp))
    ans.sort(key=lambda x:(x[1], x[0]))
    return ans[0]
