import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
M = []
dic = defaultdict(int)
for _ in range(n):
    M.append(input())
k = int(input())

for m in M:
    cnt = m.count("0") # 0의 개수
    if cnt > k:
        continue
    # 짝수 일때
    if cnt % 2 == 0:
        if k % 2 == 0:
            dic[m] += 1

    # 홀수 일때
    else:
        if k % 2 == 1:
            dic[m] += 1

if dic:
    print(max(dic.values()))
else:
    print(0)