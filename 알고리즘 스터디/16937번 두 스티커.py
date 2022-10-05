import sys
input = sys.stdin.readline

def check(s1, s2, r, c):
    if s1 <= r and s2 <= c:
        return True
    if s2 <= r and s1 <= c:
        return True
    return False

h, w = map(int, input().split())
temp = max(h, w)
n = int(input())
S = []
ans = []

for _ in range(n):
    r, c = map(int, input().split())
    if r > temp or c > temp:
        continue
    S.append((r, c, r*c))

for i in range(len(S)-1):
    r1, c1 = h-S[i][0], w
    r2, c2 = w-S[i][1], h
    r3, c3 = h-S[i][1], w
    r4, c4 = w-S[i][0], h
    for j in range(i+1, len(S)):
        if r1>=0 and c1>=0 and r2>=0 and c2>=0:
            if check(S[j][0], S[j][1], r1, c1) or check(S[j][0], S[j][1], r2, c2):
                ans.append(S[i][2] + S[j][2])
                continue
        if r3>=0 and c3>=0 and r4>=0 and c4>=0:
            if check(S[j][0], S[j][1], r3, c3) or check(S[j][0], S[j][1], r4, c4):
                ans.append(S[i][2] + S[j][2])

if ans:
    print(max(ans))
else:
    print(0)