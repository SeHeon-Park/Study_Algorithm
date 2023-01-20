from bisect import bisect_left, bisect_right

def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    ans = []
    idx = len(B)
    for b in B:
        if idx == 0:
            break
        idx_l = bisect_left(A, b)-1
        if idx_l < 0:
            break
        if idx_l >= idx:
            answer += 1
            idx -= 1
        else:
            answer += 1
            idx = idx_l
    return answer

print(solution([2,2,5,8], [8,6,2,2]))