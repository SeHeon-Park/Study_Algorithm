def get_number(n):
    word = ''
    count = 0
    while n != 0:
        temp = n % 2
        n = n // 2
        if temp == 1:
            count += 1
        word = str(temp) + word
    return word, count

def solution(n):
    answer = 0
    number, count_o = get_number(n)
    while True:
        n += 1
        number, count = get_number(n)
        if count == count_o:
            return n