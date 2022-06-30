from itertools import permutations
import math

def solution(k, dungeons):
    answer = -math.inf
    for d in permutations(dungeons):
        piro, cnt = k, 0
        for m in d:
            if piro >= m[0]:
                piro -= m[1]
                cnt += 1
            else:
                break
        if cnt == len(dungeons):
            return cnt
        answer = max(answer, cnt)
    return answer