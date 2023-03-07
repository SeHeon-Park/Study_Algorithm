import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))


dic = defaultdict(int)
cnt = 1
i1, i2 = 0, 1
dic[A[0]] += 1
B = []

while True:
    if i2 > n-1:
        B.append(cnt)
        break
    if dic[A[i2]]+1 > k:
        B.append(cnt)
        temp = A[i2]
        while True:
            if A[i1] == temp:
                dic[A[i1]] -= 1
                cnt -= 1
                i1 += 1
                break
            dic[A[i1]] -= 1
            i1 += 1
            cnt -= 1
    cnt += 1
    dic[A[i2]] += 1
    i2 += 1
print(max(B))


