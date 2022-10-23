import heapq

for t in range(10):
    n = int(input())
    MIN = [int(x) for x in input().split()]
    MAX = []
    flag = 0
    for m in MIN:
        MAX.append(-m)
    heapq.heapify(MIN)
    heapq.heapify(MAX)
    for _ in range(n):
        heapq.heappush(MAX, heapq.heappop(MAX) + 1)
        heapq.heappush(MIN, heapq.heappop(MIN) + 1)

    print("#{} {}".format(t + 1, -heapq.heappop(MAX) - heapq.heappop(MIN)))