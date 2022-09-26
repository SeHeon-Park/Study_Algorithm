# 앞에서 부터 시작해서 자신보다 앞에 있는 원소들 중 자신보다 큰 원소의 개수의 최대값을 구하는 문제였다..


# 정석 풀이
import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    a = int(input())
    A.append([a, i])

A.sort(key=lambda x:(x[0], x[1]))
ans = []

for i in range(n):
    ans.append(A[i][1] - i)

print(max(ans)+1)



# 우선순위 큐 사용 풀이
import sys
import math
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
que = PriorityQueue(maxsize=n)
ans = -math.inf

for i in range(n):
    a = int(input())
    que.put((a, (a, i)))

for i in range(n):
    ans = max(ans, que.get()[1][1]-i)

print(ans+1)

