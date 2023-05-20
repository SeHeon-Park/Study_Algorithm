from collections import defaultdict

def check(A, B):
    for k, v in A.items():
        if B[k] != v:
            return False
    return True

def solution(want, number, discount):
    answer = 0
    info = defaultdict(int)
    for w in range(len(want)):
        info[want[w]] = number[w]

    dic = defaultdict(int)
    for i in range(10):
        dic[discount[i]] += 1
    if check(info, dic):
        answer += 1
    s, e = 0, 9
    while True:
        s += 1
        e += 1
        if e > len(discount)-1:
            e -= 1
            dic[discount[s-1]] -= 1
        else:
            dic[discount[s-1]] -= 1
            dic[discount[e]] += 1
        if check(info, dic):
            answer += 1
        if e == s:
            break
    return answer
