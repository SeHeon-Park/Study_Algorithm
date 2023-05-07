def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])
    cur = routes[0][1]
    idx = 1
    while True:
        if idx > len(routes)-1:
            break
        while True:
            if idx > len(routes) - 1:
                break
            if routes[idx][0] <= cur <= routes[idx][1]:
                idx += 1
            else:
                answer += 1
                cur = routes[idx][1]
                break

    return answer