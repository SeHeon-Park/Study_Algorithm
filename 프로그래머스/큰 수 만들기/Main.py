def solution(number, k):
    answer = []
    for n in number:
        if not answer:
            answer.append(n)
            continue
        while answer[-1] < n:
            if k == 0:
                break
            k-=1
            answer.pop()
            if not answer:
                break
        answer.append(n)
        if len(answer) == len(number) - k:
            break
        
    return ''.join(answer)