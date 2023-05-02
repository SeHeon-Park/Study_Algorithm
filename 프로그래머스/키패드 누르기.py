def distance(s, e):
    return abs(s[0]-e[0]) + abs(s[1]-e[1])

def solution(numbers, hand):
    answer = ''
    dic = {1:(0, 0), 2:(0, 1), 3:(0, 2),
           4:(1, 0), 5:(1, 1), 6:(1, 2),
           7:(2, 0), 8:(2, 1), 9:(2, 2),
           0:(3, 1)}
    l_cur, r_cur = (3, 0), (3, 2)
    for n in numbers:
        target = dic[n]
        if n == 1 or n == 4 or n == 7:
            answer += "L"
            l_cur = target
            continue
        elif n == 3 or n == 6 or n == 9:
            answer += "R"
            r_cur = target
            continue
        l_distance = distance(l_cur, target)
        r_distance = distance(r_cur, target)
        if l_distance > r_distance:
            answer += "R"
            r_cur = target
        elif l_distance < r_distance:
            answer += "L"
            l_cur = target
        else:
            if hand == "left":
                answer += "L"
                l_cur = target
            else:
                answer += "R"
                r_cur = target
        print(target, l_distance, r_distance)
    return answer