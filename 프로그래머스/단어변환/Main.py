def check(curr,  next):
    count = 0
    for i in range(len(curr)):
        if curr[i] != next[i]:
            count += 1
    if count == 1:
        return 1
    else:
        return -1

def visit(begin, target, words, count, visited):
    if begin == target:
        answer.append(count)
        return
    for i in range(len(words)):
        t = check(begin, words[i])
        if t == 1 and visited[i] == 0:
            visited[i] = 1
            count += 1
            visit(words[i], target, words, count, visited)
            count -= 1
            visited[i] = 0
    return


def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]
    visit(begin, target, words, 0, visited)
    if len(answer) == 0:
        return 0
    return min(answer)

answer = []