def change_number(a, b):
    number = ''
    type = '0123456789ABCDEF'  # 코드 깔끔..
    while a > 0:
        n = type[a % b]
        # if n == 10:
        #     n = 'A'
        # elif n == 11:
        #     n = 'B'
        # elif n == 12:
        #     n = 'C'
        # elif n == 13:
        #     n = 'D'
        # elif n == 14:
        #     n = 'E'
        # elif n == 15:
        #     n = 'F'
        a = a // b
        number = str(n) + number
    return number

def solution(n, t, m, p):
    answer = ''
    temp = '0'
    cnt = 1
    while len(temp) <= t*m:
        temp += change_number(cnt, n)
        cnt += 1
    while len(answer) < t:
        answer += temp[p-1]
        p += m
    return answer