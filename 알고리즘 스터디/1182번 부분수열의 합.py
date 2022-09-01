## 백트래킹 사용

import sys
input = sys.stdin.readline
cnt = 0

def recursion(idx, ans):
    global cnt
    if idx >= len(M):
        return
    if ans+M[idx] == s:
        cnt += 1
    recursion(idx+1, ans+M[idx])
    recursion(idx+1, ans)
    return

n, s = map(int, input().split())
M = [int(x) for x in input().split()]
recursion(0, 0)
print(cnt)