import sys
input = sys.stdin.readline

def recursive(r, c, cnt, ans):
    qr, qc = r//2, c//2
    rr, rc = r%2, c%2
    if qr < 2 and qc < 2:
        return dic[(qr, qc)] * (cnt*4) + dic[(rr, rc)] * cnt
    return recursive(qr, qc, cnt*4, ans) + dic[(rr, rc)]*cnt

N, r, c = map(int, input().split())
dic = {}
dic[(0, 0)], dic[(0, 1)], dic[(1, 0)], dic[(1, 1)] = 0, 1, 2, 3
print(recursive(r, c, 1, 0))