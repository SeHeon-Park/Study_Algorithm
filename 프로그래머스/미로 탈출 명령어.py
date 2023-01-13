def solution(n, m, x, y, r, c, k):
    answer = ""
    if abs(r - x) + abs(c - y) > k:
        return "impossible"

    while True:
        if k == 0:
            if x == r and y == c:
                return answer
            else:
                return "impossible"

        if x+1<=n and abs(r - (x + 1)) + abs(c - y) <= k-1:
            x += 1
            answer += 'd'
            k -= 1
            continue
        if y-1>=1 and abs(r - x) + abs(c - (y - 1)) <= k-1:
            y -= 1
            answer += 'l'
            k -= 1
            continue
        if y+1<=m and abs(r - x) + abs(c - (y + 1)) <= k-1:
            y += 1
            answer += 'r'
            k -= 1
            continue
        if x-1>=1 and abs(r - (x - 1)) + abs(c - y) <= k-1:
            x -= 1
            answer += 'u'
            k -= 1
            continue
        return "impossible"