from collections import defaultdict

def solution(clothes):
    ans = 1
    dic = defaultdict(int)
    for c in clothes:
        dic[c[1]] += 1
    for d in dic.values():
        ans *= (d+1)
    return ans-1
