def parent(P, a):
    if a != P[a]:
        P[a] = parent(P, P[a])
    return P[a]

def union(P, a, b):
    a = parent(P, a)
    b = parent(P, b)
    if a == b:
        return False
    if a < b:
        P[b] = a
    else:
        P[a] = b
    return True

def solution(n, costs):
    ans = 0
    P = [x for x in range(n)]
    costs.sort(key=lambda x:x[2])
    cnt = 0
    for s, e, c in costs:
        if union(P, s, e):
            cnt += 1
            ans += c
        if cnt == n:
            break
    return ans