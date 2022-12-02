def solution(alp, cop, problems):
    max_alp = -100
    max_cop = -100
    for i in range(len(problems)):
        if problems[i][0] - alp < 0:
            problems[i][0] = 0
        else:
            problems[i][0] = problems[i][0] - alp
        if problems[i][1] - cop < 0:
            problems[i][1] = 0
        else:
            problems[i][1] = problems[i][1] - cop
        max_alp = max(max_alp, problems[i][0])
        max_cop = max(max_cop, problems[i][1])

    if max_alp <= 0 and max_cop <= 0:
        return 0
    dp = [[int(x + y) for x in range(max_cop+1)] for y in range(max_alp+1)]

    for i in range(max_alp + 1):
        for j in range(max_cop + 1):
            for p in problems:
                if p[0] <= i and p[1] <= j:
                    # (처음부터 혼자 공부, 문제 풀어서 공부, 해당 문제부터 혼자 공부)
                    if i + p[2] > max_alp and j + p[3] <= max_cop:
                        dp[max_alp][j + p[3]] = min(dp[max_alp][j + p[3]], dp[i][j] + p[4], dp[i][j] + p[2] + p[3])
                    elif j + p[3] > max_cop and i + p[2] <= max_alp:
                        dp[i + p[2]][max_cop] = min(dp[i + p[2]][max_cop], dp[i][j] + p[4], dp[i][j] + p[2] + p[3])
                    elif i + p[2] > max_alp and j + p[3] > max_cop:
                        dp[max_alp][max_cop] = min(dp[max_alp][max_cop], dp[i][j] + p[4], dp[i][j] + p[2] + p[3])
                    else:
                        dp[i + p[2]][j + p[3]] = min(dp[i + p[2]][j + p[3]], dp[i][j] + p[4], dp[i][j] + p[2] + p[3])
    return dp[max_alp][max_cop]
