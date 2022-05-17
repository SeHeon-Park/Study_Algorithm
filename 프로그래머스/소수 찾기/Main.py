from itertools import permutations
import math

def isprime(a):
    if a == 0 or a == 1:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    c = ''
    for j in range(1, len(numbers)+1):
        arr = permutations(numbers, j)
        for n in arr:
            for i in range(len(n)):
                c += n[i]
            if isprime(int(c)):
                answer.append(int(c))
            c = ''
    return len(set(answer))

# permutations: 순열, combination: 조합(순열에서 중복 제거된 것)
# 소수 판별할때 121, 225와 같이 완전제곱으로 이루어진 것 확인