import sys
input = sys.stdin.readline

def find_cnt(temp):
    cnt = 0
    for a in A:
        cnt += (a//temp)
    return cnt

k, n = map(int, input().split())
A = []
ans = []

for _ in range(k):
    A.append(int(input()))

A.sort()
l, r = 1, A[-1]+1

while l<=r:
    m = (l+r)//2
    if n > find_cnt(m):
        r = m
    else:
        if m in ans:
            break
        ans.append(m)
        l = m

print(max(ans))