import sys
input = sys.stdin.readline

n = int(input())
P = [int(x) for x in input().split()]
temp = 0
ans = 0
P.sort()

for p in P:
    temp += p
    ans += temp
print(ans)