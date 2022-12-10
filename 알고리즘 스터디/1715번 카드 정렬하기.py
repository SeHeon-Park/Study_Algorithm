import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

n = int(input())
C = []
for _ in range(n):
    C.append(int(input()))
ans = 0
heapify(C)

while C:
    if len(C) == 1:
        break
    s = heappop(C)+heappop(C)
    ans += s
    heappush(C, s)
print(ans)

