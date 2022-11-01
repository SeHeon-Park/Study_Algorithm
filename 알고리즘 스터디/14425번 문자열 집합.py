import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = set()
cnt = 0

for _ in range(n):
    S.add(input())

for _ in range(m):
    a = input()
    if a in S:
        print(a, S)
        cnt += 1

print(cnt)