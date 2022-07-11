from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    deq = deque(people)
    l, r = 0, len(people)-1
    while len(deq) > 1:
        l, r = 0, len(deq)-1
        if deq[l]+deq[r] > limit:
            deq.pop()
            answer += 1
        else:
            deq.popleft()
            deq.pop()
            answer += 1
    if deq:
        answer += 1
    return answer