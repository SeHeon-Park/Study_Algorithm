def check(front, back, words):
    if front[-1] != back[0]:
        return False
    if back in words:
        return False
    if len(back) == 1 or len(front) == 1:
        return False
    return True

def solution(n, words):
    answer = []
    turn = 1
    count = 1
    for i in range(len(words)-1):
        count += 1
        if count == n+1:
            turn += 1
            count = 1
        if not check(words[i], words[i + 1], words[:i+1]):
            return [count, turn]

    return [0,0]