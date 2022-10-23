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
<<<<<<< HEAD
        heapq.heappush(MAX, heapq.heappop(MAX) + 1)
        heapq.heappush(MIN, heapq.heappop(MIN) + 1)

    print("#{} {}".format(t + 1, -heapq.heappop(MAX) - heapq.heappop(MIN)))
=======
        a = heapq.heappop(MAX)
        b = heapq.heappop(MIN)
        if -a-b <= 1:
            flag = 1
            break
        heapq.heappush(MAX, a + 1)
        heapq.heappush(MIN, b + 1)
    if flag:
        print("#{} {}".format(t + 1, -a - b))
    else:
        print("#{} {}".format(t + 1, -heapq.heappop(MAX) - heapq.heappop(MIN)))
>>>>>>> 8c3b3446c3a2a3746a233e8a2f6e34d7517625ab
