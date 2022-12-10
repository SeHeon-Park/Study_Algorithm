def solution(queue1, queue2):
    answer = 0
    S = sum(queue1) + sum(queue2)
    M = queue1 + queue2
    if S % 2 != 0:
        return -1
    target = S//2
    s, e = 0, len(queue1)-1
    cur = sum(queue1)
    while True:
        if cur == target:
            return answer
        elif cur > target:
            cur -= M[s]
            s += 1
        else:
            e += 1
            # e가 0으로 돌아오면 결국 같아짐
            if e > len(M)-1:
                return -1
            cur += M[e]
        answer += 1