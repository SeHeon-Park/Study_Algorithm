# LIS O(n^2) 풀이 6144ms (dp)
import sys
input = sys.stdin.readline

n = int(input())
M = [int(x) for x in input().split()]
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i-1, -1, -1):
        if M[i] > M[j]:
            dp[i] = max(dp[i], dp[j]+1)


print(max(dp))


# LIS O(nlogn)풀이 200ms (이분탐색, 수열까지 구하기)
import sys
from bisect import bisect_right
input = sys.stdin.readline

n = int(input())
M = [int(x) for x in input().split()]
arr = [M[0]]
I = [0]

for i in range(1, n):
    idx = bisect_right(arr, M[i])
    I.append(idx)
    if idx > len(arr)-1:
        arr.append(M[i])
    else:
        arr[idx] = M[i]

t = len(arr)-1
ans = []

# 트레이싱을 통해 수열까지 구하기
for i in range(n-1, -1, -1):
    if I[i] == t:
        ans.append(M[i])
        t -= 1

print(ans)
print(len(arr))



