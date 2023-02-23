def solution(relation):
    ans = 0
    l = len(relation[0])
    K = []

    def combination(idx, s):
        if len(s) == i:
            S.append(s)
            return
        for j in range(idx, l):
            if include(s+[j]):
                continue
            combination(j+1, s+[j])

    def check():
        T = set()
        for r in relation:
            temp = ""
            for p in s:
                temp += r[p]
            if temp in T:
                return False
            T.add(temp)
        return True

    def include(A):
        for k in K:
            l = 0
            for a in A:
                if a in k:
                    l += 1
            if l == len(k):
                return True
        return False

    for i in range(1, l+1):
        S = []
        combination(0, [])
        for s in S:
            if check():
                K.append(s)
                ans += 1
    return ans