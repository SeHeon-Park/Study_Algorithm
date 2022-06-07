import math

def compare(split_s, cnt):  # count만큼 비교
    answer = 0
    c = 0
    for i in range(1, len(split_s)): # 마지막 데이터가 다르면 답 틀려..
        if split_s[i-1] == split_s[i]:
            c += 1
        if i == len(split_s)-1:
            if c == 0:
                answer += cnt
            else:
                answer += (cnt + len(str(c + 1)))
            break
        if split_s[i-1] != split_s[i]:
            if c == 0:
                answer += cnt
            else:
                answer += (cnt + len(str(c + 1)))
            c = 0
    if split_s[i-1] != split_s[i]:
        answer += len(split_s[-1])
    return answer

def solution(s):
    if len(s) == 1: # 단어가 1개일때 예외처리
        return 1
    cnt = 1
    answer = math.inf
    split_s = []
    while cnt != math.floor(len(s)/2)+1:
        for i in range(0, len(s), cnt):
            split_s.append(s[i:i + cnt])
        answer = min(compare(split_s, cnt), answer)
        cnt += 1
        split_s.clear()
    return answer