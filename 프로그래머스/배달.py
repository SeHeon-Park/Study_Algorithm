from collections import defaultdict
from heapq import heappush, heappop
import math

def solution(N, road, K):
    dic = defaultdict(dict)
    for r in road:
        if r[1]-1 in dic[r[0]-1].keys() and dic[r[0]-1][r[1]-1] <= r[2]:
            continue
        dic[r[0]-1][r[1]-1] = r[2]
        dic[r[1]-1][r[0]-1] = r[2]

    dist = [math.inf for _ in range(N)]
    dist[0] = 0

    H = []
    H.append((0, 0))
    while H:
        w, t = heappop(H)
        for town, weight in dic[t].items():
            if w+weight < dist[town]:
                dist[town] = w+weight
                heappush(H, (w+weight, town))
    ans = 0
    for d in dist:
        if d <= K:
            ans += 1
    return ans
