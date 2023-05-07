import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dic = defaultdict(int)
ans = []
for _ in range(n):
    info = input()[:-1].split(".")
    dic[info[1]] += 1

for k, v in dic.items():
    ans.append([k, v])

ans.sort(key=lambda x:x[0])

for a in ans:
    print(a[0], a[1])
