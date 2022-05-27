import math

def check(progress, speeds):
    count = 0
    for i in range(len(progress)-1, -1, -1):
        if progress[i] >= 100:
            count += 1
            progress.pop()
            speeds.pop()
        else:
            break
    answer.append(count)
    return progress, speeds


def solution(progresses, speeds):
    progresses.reverse()
    speeds.reverse()
    while len(progresses) != 0:
        p = 100 - progresses[-1]  # 맨앞 남은 퍼센트
        d = math.ceil(p/speeds[-1])  # 맨앞 남은 날짜
        for i in range(len(progresses)):
            progresses[i] += d * speeds[i]
        progresses, speeds = check(progresses, speeds)
    return answer

answer = []