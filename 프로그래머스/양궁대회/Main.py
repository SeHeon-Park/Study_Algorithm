import math

def find_min(info):
    for i in range(10, -1, -1):
        flag = 0
        info.sort(key = lambda x : x[i], reverse=True)
        m = info[0][i]
        for j in info:
            if j[i] < m:
                flag = 1
                break
        if flag == 1:
            break
    return info[0]
            
            
def bfs(ryan, info, index, k, Max):
    if k < 0:
        return Max
    if k == 0:
        apeach_score = get_score(info)
        ryan_score = get_score(ryan)
        if ryan_score > apeach_score and Max <= ryan_score-apeach_score:
            r = ryan.copy()
            Max = ryan_score - apeach_score
            ryan_info.append([r, Max])
        return Max
    if index == 10:
        temp = info[index] 
        ryan[index] = k
        info[index] = 0
        apeach_score = get_score(info)
        ryan_score = get_score(ryan)
        if ryan_score > apeach_score and Max <= ryan_score-apeach_score:
            r = ryan.copy()
            Max = ryan_score-apeach_score
            ryan_info.append([r, Max])
        ryan[index] = 0
        info[index] = temp
        return Max
    m = info[index]+1
    ryan[index] = m
    info[index] = 0
    Max = bfs(ryan, info, index+1, k-m, Max)
    ryan[index] = 0
    info[index] = m-1
    Max = bfs(ryan, info, index+1, k, Max)
    return Max

def get_score(info):
    score = 0
    count = 10
    for i in info:
        if i == 0:
            count -= 1
            continue
        score += count
        count -= 1
    return score

def solution(n, info):
    answer = []
    global ryan_info
    ryan_info = []
    Max = bfs([0,0,0,0,0,0,0,0,0,0,0], info, 0, n, -math.inf)
    if len(ryan_info) == 0:
        return [-1]

    for r in ryan_info:
        if r[1] == Max:
            answer.append(r[0])

    if len(answer) == 1:
        return answer[0]
    else:
        return find_min(answer)