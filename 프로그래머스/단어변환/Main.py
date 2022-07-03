def check(s, n):
    index = 0
    cnt = 0
    while index != len(s):
        if cnt > 1:
            return False
        if s[index] != n[index]:
            cnt += 1
        index += 1
    if cnt == 1:
        return True
    return False

def recursive(curr, target, words, cnt):
    if curr == target:
        answer.append(cnt)
        return
    for i in range(len(words)):
        if check(curr, words[i]):
            recursive(words[i], target, words[:i]+words[i+1:], cnt+1)
    return

def solution(begin, target, words):
    global answer
    answer = []
    if not target in words:
        return 0
    recursive(begin, target, words, 0)
    return min(answer)