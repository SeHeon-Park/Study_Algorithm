def solution(brown, yellow):
    xpy = int((brown + 4) / 2)
    for i in range(1, xpy):
        x, y = i, xpy-i
        if x*y == yellow+brown:
            if x >= y:
                answer = [x, y]
            else:
                answer = [y, x]
            break
    return answer