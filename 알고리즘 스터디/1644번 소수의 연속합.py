import sys
input = sys.stdin.readline

n = int(input())
M = [int(x) for x in range(n+1)]
S = []

# 에라토스테네스의 체
for i in range(2, n+1):
    if M[i] == 0: continue
    else:
        for j in range(i, n+1, i):
            M[j] = 0
        S.append(i)

if not S:
    print(0)
else:
    r = len(S)-1
    l = len(S)-2

    ans = 0
    if S[r] == n:
        ans += 1

    temp = S[l]+S[r]
    while True:
        if l<0: break
        if temp == n:
            ans += 1
        elif temp < n:
            l_temp = l
            while True:
                if l_temp < 0:
                    break
                if temp == n:
                    ans += 1
                    break
                elif temp > n:
                    break
                l_temp -= 1
                temp += S[l_temp]
        r -= 1
        l -= 1
        temp = S[l] + S[r]


    print(ans)