def check(place):
    xt = [0, 1, 1, -1]
    yt = [1, 0, 1, 1]
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                for t in range(4):
                    cnt, x, y = 0, i, j
                    while cnt < 2:
                        x += xt[t]
                        y += yt[t]
                        cnt += (abs(xt[t]) + abs(yt[t]))
                        if 0 <= x <= 4 and 0 <= y <= 4:
                            if place[x][y] == 'P':
                                if t == 2 :
                                    if x-1 >= 0 and place[x-1][y] == 'O':
                                        return 0
                                    elif y-1 >= 0 and place[x][y-1] == 'O':
                                        return 0
                                    else:
                                        continue
                                if t == 3:
                                    if x+1 <= 4 and place[x+1][y] == 'O':
                                        return 0
                                    elif y-1 >= 0 and place[x][y-1] == 'O':
                                        return 0
                                    else:
                                        continue
                                return 0
                            if place[x][y] == 'X':
                                break
                        else:
                            break
    return 1

def solution(places):
    answer = []
    for i in range(len(places)):
        c = check(places[i])
        answer.append(c)
    return answer

# BFS는 좌표 이동하기가 good!