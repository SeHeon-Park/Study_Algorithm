import sys
import re
input = sys.stdin.readline

def change(P):
    if P == "S":
        return 1
    if P == "D":
        return 2
    if P == "T":
        return 3

def solution(dartResult):
    B = re.split(r"[0-9]", dartResult)
    A = re.split(r"[^0-9]", dartResult)
    info = [[] for _ in range(3)]
    ans = [1 for _ in range(3)]

    # 숫자
    idx = 0
    idx_i = 0
    while True:
        if idx > len(A)-1:
            break
        if A[idx] != '':
            info[idx_i].append(A[idx])
            idx_i += 1
        idx += 1

    # 문자
    idx = 0
    idx_i = 0
    while True:
        if idx > len(B) - 1:
            break
        if B[idx] != '':
            info[idx_i].append(B[idx])
            idx_i += 1
        idx += 1

    for i in range(2, -1, -1):
        number = int(info[i][0])
        op = info[i][1]

        a = re.sub(r"[^A-Z]", "", op)
        b = re.sub(r"[A-Z]", "", op)
        ans[i] = ans[i]*(number**change(a))
        if b == "*":
            cnt = 0
            for j in range(i, -1, -1):
                if cnt == 2:
                    break
                ans[j] = ans[j]*2
                cnt += 1
        if b == "#":
            ans[i] = ans[i]*(-1)
    return sum(ans)
