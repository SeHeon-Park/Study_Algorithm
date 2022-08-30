# combinations 내장함수를 사용하면 쉽게 해결 가능 하지만
# 내장함수를 못쓴다고 하면 조합을 구하는 함수를 직접 구현해야함

import sys

def combination(A, ans):
    if len(ans) == 6:
        for a in ans:
            print(a, end=' ')
        print()
        return
    for i in range(len(A)):
        combination(A[i+1:], ans+[A[i]])
    return

M = []

while True:
    M = [int(x) for x in sys.stdin.readline().split()]
    if M[0] == 0:
        break
    M = M[1:]
    combination(M, [])
    print()
