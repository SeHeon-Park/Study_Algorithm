def distance(v1, v2):
    return abs(v1[0]-v2[0]) + abs(v1[1]-v2[1])

def solution(numbers, hand):
    answer = ''
    l, r = (3,0), (3,2)
    key = [(3,1), (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    for n in numbers:
        if n % 3 == 1 and n != 0:
            answer += 'L'
            l = key[n]
            continue
        elif n % 3 == 0 and n != 0:
            answer += 'R'
            r = key[n]
            continue
        dl = distance(key[n], l)
        dr = distance(key[n], r)
        if dl < dr:
            answer += 'L'
            l = key[n]
        elif dl > dr:
            answer += 'R'
            r = key[n]
        else:
            if hand == "right":
                answer += 'R'
                r = key[n]
            else:
                answer += 'L'
                l = key[n]
    return answer