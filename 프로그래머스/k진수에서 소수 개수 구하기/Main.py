import math

def isprime(prime):
    if prime == 1:
        return False
    for i in range(2, int(math.sqrt(prime))+1):  # math.sqrt : 제곱근
        if prime % i == 0:
            return False
    return True

def make_number(n, k):
    number = ''
    while n != 0:
        number = str(n%k) + number
        n = n // k
    return number    

def solution(n, k):
    number = make_number(n, k)
    word = ''
    answer = 0
    for p in number:
        if p == '0':
            if len(word) != 0 and isprime(int(word)):
                answer += 1
            word = ''
            continue
        word += p
    if len(word) != 0 and isprime(int(word)):
        answer += 1
    return answer