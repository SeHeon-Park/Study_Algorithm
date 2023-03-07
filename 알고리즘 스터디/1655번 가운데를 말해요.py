## 한층 성장한 나의 풀이 ^^
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

H_max = []
H_min = []
H = []

c = int(input())
check = [0 for _ in range(c)]

for i in range(c):
    n = int(input())
    H.append(n)

a, b = max(H[0], H[1]), min(H[0], H[1])
print(H[0])
print(b)
H_max.append(-b)
H_min.append(a)

for i in range(2, c):
    target = H[i]
    if H_min[0] >= target:
        heappush(H_max, -target)
    else:
        heappush(H_min, target)
    if len(H_max) - len(H_min) == 2:
        heappush(H_min, -heappop(H_max))
    elif len(H_min) > len(H_max):
        heappush(H_max, -heappop(H_min))
    print(-H_max[0])


## 옛날 풀이
import heapq
import sys

n = int(sys.stdin.readline())
heapMin = []
heapMax = []

for i in range(n):
    number = int(sys.stdin.readline())
    if len(heapMin) == 0 and len(heapMax) == 0:
        heapq.heappush(heapMax, -number)
    elif len(heapMin) == len(heapMax):
        if heapMin[0] <= number:
            heapq.heappush(heapMax, -heapq.heappop(heapMin))
            heapq.heappush(heapMin, number)
        else:
            heapq.heappush(heapMax, -number)
    elif len(heapMin) != len(heapMax):
        if -heapMax[0] >= number:
            heapq.heappush(heapMin, -heapq.heappop(heapMax))
            heapq.heappush(heapMax, -number)
        else:
            heapq.heappush(heapMin, number)
    print(-heapMax[0])


## 정석 풀이
import heapq
import sys

n = int(sys.stdin.readline())

leftHeap = []
rightHeap = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])