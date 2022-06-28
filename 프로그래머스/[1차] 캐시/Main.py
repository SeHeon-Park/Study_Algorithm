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


- LRU(Least Recently Used)
가장 오랫동안 참조하지 않은 페이지를 캐시에서 교체하는 것
- LFU(Least Frequently Used)
가장 적게 참조한 페이지를 캐시에서 교체하는 것

[캐시 적중] 
이미 캐시에 있던 페이지를 가장 처음으로 가져온다.

[캐시 미스]
- 캐시가 가득 찬 경우
가장 뒤(참조한지 가장 오래된)의 페이지를 삭제하고 가장 앞에 새 페이지를 삽입한다.
- 캐시에 자리가 있는 경우
가장 앞에 새 페이지를 삽입한다.