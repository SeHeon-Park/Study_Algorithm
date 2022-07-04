def solution(n,a,b):
    answer = 1
    while True:
        if abs(a-b) == 1 and (a//2 != b//2):
            break
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1
        a = a//2
        b = b//2
        answer += 1
    return answer