def check(idx):
    si = 0
    if idx+len(s) > len(m):
        return False
    for i in range(idx, idx+len(s)):
        if s[si] != m[i]:
            return False
        si += 1
    return True

while True:
    try:
        t = int(input())
        s = input()
        m = input()
        ans = 0
        for i in range(len(m)):
            if s[0] == m[i]:
                if check(i):
                    ans += 1
        print("#{} {}".format(t, ans))
    except:
        break
