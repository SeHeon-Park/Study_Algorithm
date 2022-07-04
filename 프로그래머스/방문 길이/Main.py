from collections import defaultdict

def change(d):
    if d == 'U':
        return 'D'
    if d == 'D':
        return 'U'
    if d == 'R':
        return 'L'
    if d == 'L':
        return 'R'


def solution(dirs):
    answer = 0
    visit = [[0 for _ in range(11)] for _ in range(11)]
    dic = {'U':[0, -1], 'D':[0, 1], 'R':[1, 0], 'L':[-1, 0]}
    check = defaultdict(list)
    x, y = 5, 5
    for d in dirs:
        fx = x
        fy = y
        x += dic[d][0]
        y += dic[d][1]
        if x<0 or x>10 or y<0 or y>10:
            x -= dic[d][0]
            y -= dic[d][1]
            continue
        if visit[fy][fx] == 1 and visit[y][x] == 1:
            if (y, x) in check.keys():
                if change(d) in check[(y, x)]:
                    continue
        answer += 1
        visit[y][x] = 1
        visit[fy][fx] = 1
        check[(fy, fx)].append(d)
        check[(y, x)].append(change(d))       
    return answer