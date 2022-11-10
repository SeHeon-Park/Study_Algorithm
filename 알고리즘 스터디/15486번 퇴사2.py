import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
T = defaultdict(set)
dp = [0 for _ in range(n+1)]
for i in range(n):
    t, p = tuple(map(int, input().split()))
    if i+t > n:
        continue
    T[i+t].add((i+1, p))

for i in range(1, n+1):
    if not T[i]:
        dp[i] = dp[i-1]
    for t in T[i]:
        dp[i] = max(dp[t[0]-1]+t[1], dp[i-1], dp[i])

print(dp[-1])
