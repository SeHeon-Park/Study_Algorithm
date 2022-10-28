import sys
from collections import defaultdict
input = sys.stdin.readline

while True:
    N = list(map(int, input().split()))
    M = []
    ans = -1
    if not N[0]:
        break

