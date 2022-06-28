import re

def solution(files):
    sub_file = []
    answer = []
    for f in files:
        head = re.split("[0-9]", f)[0].upper()
        number = re.findall("[0-9]+", f)[0]  # 튜플문제 주석 참고, findall(원하는 패턴 찾아 리스트로 만듦)
        n, d = 0, 1
        for i in range(len(number)):
            n += d * int(number[len(number)-i-1])
            d *= 10
        sub_file.append([head, n, f])
    sub_file.sort(key = lambda x : (x[0], x[1]))
    for s in sub_file:
        answer.append(s[2])
    return answer