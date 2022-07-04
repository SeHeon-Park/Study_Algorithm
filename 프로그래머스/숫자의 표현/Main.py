def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        cnt, num = 0, i
        while cnt < n:
            cnt += num
            num += 1
        if cnt == n:
            answer += 1
    return answer