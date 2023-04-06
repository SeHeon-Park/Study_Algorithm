import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dic = defaultdict(int)
    ans = 1
    for _ in range(n):
        a, b = map(str, input().split())
        dic[b] += 1
    for d in dic.values():
        ans *= (d+1)
    print(ans-1)



