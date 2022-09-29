import sys
input = sys.stdin.readline

def find_tree(t):
    length = 0
    for a in A:
        if a-t > 0:
            length += a-t
    return length

N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = []
A.sort()

l, r = 0, A[-1]

while l <= r:
    m = (l + r) // 2
    if find_tree(m) >= M:
        if m in ans:
            break
        ans.append(m)
        l = m
    else:
        r = m

print(max(ans))