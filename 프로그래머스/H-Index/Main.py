from bisect import bisect_left

def solution(citations):
    citations.sort()
    answer = citations[-1]
    while True:
        index = bisect_left(citations, answer)
        if len(citations)-index >= answer >= index: break
        answer -= 1
    return answer