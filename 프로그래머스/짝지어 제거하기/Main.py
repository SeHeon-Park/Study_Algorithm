def solution(s):
    answer = [s[0]]
    for i in range(1, len(s)):
        if not answer:
            answer.append(s[i])
            continue
        if s[i] == answer[-1]:
            answer.pop()
            continue
        answer.append(s[i])
    if answer:
        return 0
    return 1