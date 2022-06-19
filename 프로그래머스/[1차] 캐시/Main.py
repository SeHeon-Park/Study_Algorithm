from collections import deque

def solution(cacheSize, cities):
    deq = deque()
    # deq = deque(maxlen=cacheSize)  # maxlen을 통해 최대사이즈 설정 가능
    answer = 0
    for c in cities:
        c = c.upper()  # 대문자로 변환
        # c = c.lower()  # 소문자로 변환
        if c in deq:
            answer += 1
            deq.remove(c)
            deq.append(c)
            continue
        if not c in deq:
            answer += 5
            deq.append(c)
        if len(deq) == cacheSize+1:
            deq.popleft()
    return answer