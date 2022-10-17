import sys, heapq
input = sys.stdin.readline

A = []
t = int(input())
for _ in range(t):
    n = int(input())
    if n:
        heapq.heappush(A, n)
    else:
        if A:
            print(heapq.heappop(A))
        else:
            print(0)