def solution(s):
    bracket = []
    for i in s:
        if i == '(':
            bracket.append(i)
        else:
            if bracket:
                bracket.pop()
            else:
                return False
    if bracket:
        return False
    return True