import sys, re
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input()[:-1]
    n = int(input())
    s = input()[:-1].replace('[', '').replace(']', '')
    s = re.split('[,]', s)
    l, r = 0, n-1
    cnt, flag = 0, 0
    for w in p:
        if w == 'R':
            cnt += 1
        else:
            if l > r:
                flag=1
                break
            if cnt % 2 == 0:
                l += 1
            else:
                r -= 1
    if flag:
        print("error")
    else:
        if cnt % 2 == 0:
            print('['+','.join(s[l:r+1])+']')
        else:
            print('['+','.join(s[l:r+1][::-1])+']')