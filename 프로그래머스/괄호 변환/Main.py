def correct(p):  # 올바른 문자열인지 확인
    if p[0] == ')':
        return False
    word = []
    for i in p: # 스택을 써도 되지만 내장함수를 못쓰는 경우 리스트로 해결
        if i == '(':
            word.append(i)
        else:
            if len(word) == 0:
                return False
            word.pop()
    if len(word) == 0:
        return True
    else:
        return False


def solution(p):
    if len(p)==0 or correct(p):
        return p
    u, v = '', ''
    left, right = 0, 0
    for i in range(len(p)): # p를 u와 v로 분리
        if p[i] == ')':
            right += 1
        else:
            left += 1
        u += p[i]
        if left != 0 and right == left:
            break
    v = solution(p[i + 1:])
    if u[0] == '(':  # u가 올바른 괄호 문자열이면
        return u + v
    else:            # u가 올바른 괄호 문자열이 아니면
        word = '(' + v + ')'
        u = u[1:len(u) - 1]
        for i in range(len(u)):
            if u[i] == ')':
                word += '('
            else:
                word += ')'
        return word