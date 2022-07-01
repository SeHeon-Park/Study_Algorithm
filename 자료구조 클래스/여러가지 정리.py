from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from collections import deque

문자열의 sort는 알파벳 정렬이다! (예 'ABC' < 'AD') ('123' < '13')
math.ceil: 올림, math.floor: 내림, math.round: 반올림, math. sqrt: 제곱근
deq = deque(maxlen=cacheSize) : 최대사이즈 설정 가능
문자열 자체를 정렬 할때는 sorted("문자열") (리스트로 나옴)
re.split("\s", list)  # 공백에 따라 나누기
number = re.sub(r'[^0-9]', '', q)  # 숫자만 추출
q = re.sub(r'[0-9]', '', q)        # 숫자만 없애기
.isalpha() : 알파벳인지 확인
ord: str -> int, chr: int -> str : 아스키

# 정규표현식
문자 집합: \w \W, \d \D, \s \S, \b \B
1. \w, \W: 단어 문자, 비 단어 문자
2. \d, \D: 숫자 문자, 비 숫자 문자
3. \s, \S: 공백 문자, 비 공백 문자
4. \b, \B: 단어 경계, 비 단어 경계

def bisect_left(A, t):
    l = 0
    r = len(A)-1
    while l < r:
        m = (l+r) // 2
        if t > A[m]:
          l = m + 1
        else:
          r = m
    return l

def bisect_right(A, t):
    l = 0
    r = len(A) - 1
    while l < r:
        m = (l + r) // 2
        if t < A[m]:
          r = m
        else:
          l = m + 1
    return l