from bisect import bisect_left, bisect_right

def solution(N, stages):
    answer = []
    fail = []
    stages.sort()
    for i in range(1, N+1):
        idx = bisect_right(stages, i-1)
        cnt = bisect_right(stages, i) - bisect_left(stages, i)
        n = len(stages) - idx

        if n == 0:
            fail.append([i, 0])
        else:
            fail.append([i, cnt / n])

    fail.sort(key=lambda x:-x[1])
    for f in fail:
        answer.append(f[0])
    return answer
