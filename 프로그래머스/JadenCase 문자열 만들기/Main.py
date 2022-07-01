import re

def solution(s):
    answer = ''
    word = re.split(" ", s)
    for w in word:
        if w == '':
            answer += ' '
            continue
        if not w[0].isalpha:
            answer += (w + ' ')
            continue
        if len(w) == 1:
            answer += (w[0].upper() + ' ')
            continue
        answer += (w[0].upper() + w[1:].lower() + ' ')
    return answer[:-1]