import sys
input = sys.stdin.readline

A = []
n = int(input())
people = 0
for _ in range(n):
    x, a = map(int, input().split())
    A.append([x, a])
    people += a
A.sort(key=lambda x:x[0])

cnt = 0
for v, p in A:
    cnt += p
    if cnt >= people/2:
        print(v)
        break
