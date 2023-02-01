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


# 정석 풀이

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