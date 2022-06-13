def solution(s):
    result, part, answer = [], [], []
    s = s[1:-1]
    save = re.split('[},]+', s)[:-1]
    part.append(int(save[0][1:]))
    for s in range(1, len(save)):
        if save[s][0] == '{':
            result.append(part)
            part = []
            part.append(int(save[s][1:]))
            continue
        part.append(int(save[s]))
    result.append(part)
    result.sort(key = lambda x:len(x))
    for r in result:
        for i in r:
            if not i in answer:
                answer.append(i)
    return answer

## 다른 풀이
# 그냥 원소의 갯수가 가장 많은 순서대로 리스트에 담으면 되는 문제 였다.. ㅠ
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter

## 정규표현식
# 문자 집합: \w \W, \d \D, \s \S, \b \B
# 1. \w, \W: 단어 문자, 비 단어 문자
# 2. \d, \D: 숫자 문자, 비 숫자 문자
# 3. \s, \S: 공백 문자, 비 공백 문자
# 4. \b, \B: 단어 경계, 비 단어 경계