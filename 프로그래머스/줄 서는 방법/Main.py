def solution(n, k):
    if n == 1:
        return [1]
    if n == 2 and k == 1:
        return [1, 2]
    if n == 2 and k == 2:
        return [2, 1]
    answer = []
    number = [i + 1 for i in range(n)]
    dp = [0 for _ in range(n)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n):
        dp[i] = dp[i - 1] * i
    for i in range(n - 1, 0, -1):
        r = k // dp[i]
        k = k % dp[i]
        if k == 0:
            answer.append(number.pop(r-1))
        else:
            answer.append(number.pop(r))
    answer += number
    return answer