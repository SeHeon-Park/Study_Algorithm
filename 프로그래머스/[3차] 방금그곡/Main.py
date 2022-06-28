import re

def change(m):  # '#'을소문자로 바꾸기
    m = list(m)
    word = ''
    for i in range(len(m)):
        if m[i] == '#':
            m[i-1] = m[i-1].lower()
    m = "".join(m)  # 'a'.join([1,2,3]) => 1a2a3a (리스트=>str), (str=>str X)
    m = re.sub('#', '', m)
    return m

def find_minute(s, f, m):
    s = re.split(':', s)
    f = re.split(':', f)
    m = change(m)
    minute = 60*(int(f[0])-int(s[0])) + (int(f[1])-int(s[1]))
    quotient = minute // len(m)
    remainder = minute % len(m)
    info = m*quotient + m[:remainder]
    return info, minute

def solution(m, musicinfos):
    m = change(m)
    answer = []
    cnt = 0
    for a in musicinfos:
        info = re.split(',', a)
        word, minute = find_minute(info[0], info[1], info[3])
        if m in word:
            answer.append([cnt, minute, info[2]])  # 순서, 재생시간, 제목
        cnt += 1
    if answer:
        answer.sort(key=lambda x: (-x[1], x[0]))  # (1순위 조건, 2순위 조건), -붙이면 내림차순으로
        return answer[0][2]
    return "(None)"


re.sub  VS  str.replace()  => 상황에 따라 편한것 선택