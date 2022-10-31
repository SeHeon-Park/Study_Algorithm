import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = set()
cnt = 0

for _ in range(n):
    S.add(input())

for _ in range(m):
    if input() in S:
        cnt += 1

print(cnt)