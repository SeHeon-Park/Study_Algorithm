import sys
input = sys.stdin.readline

def recursive(n, start, end):
    if n == 1:
        print(start, end=" ")
        print(end)
    else:
        recursive(n-1, start, 6-(start+end))
        print(start, end=" ")
        print(end)
        recursive(n-1, 6-(start+end), end)

n = int(input())
print(2**n-1)
recursive(n, 1, 3)