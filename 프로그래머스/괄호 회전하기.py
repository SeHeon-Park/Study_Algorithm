dic = {"[":"]", "{":"}", "(":")", "]":-1, "}":-1, ")":-1}

def check(S):
    temp = []
    for p in S:
        if not temp:
            temp.append(p)
        else:
            if dic[temp[-1]] == p:
                temp.pop()
            elif dic[temp[-1]] == -1:
                return False
            else:
                temp.append(p)
    if temp:
        return False
    else:
        return True

def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        if check(s):
            answer += 1
        s = s[1:] + [s[0]]
    return answer