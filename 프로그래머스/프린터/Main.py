from collections import deque

def solution(priorities, location):
    answer = 1
    deq1 = deque(priorities)
    deq2 = deque([i for i in range(len(priorities))])
    while True:
        index = deq1.index(max(deq1))
        for i in range(index):
            deq1.append(deq1.popleft())
            deq2.append(deq2.popleft())
        if deq2[0] == location:
            break
        deq1.popleft()
        deq2.popleft()
        answer += 1
    return answer