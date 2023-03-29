import sys
input = sys.stdin.readline

def find_parents(a):
    if a != P[a]:
        P[a] = find_parents(P[a])
    return P[a]

def union(a, b):
    a = find_parents(a)
    b = find_parents(b)
    if a < b:
        P[b] = a
    else:
        P[a] = b

g = int(input())
p = int(input())
P = [int(i) for i in range(g+1)]
cnt = 0

for _ in range(p):
    n = int(input())
    idx = find_parents(n)
    if idx == 0:
        break
    cnt += 1
    union(idx, idx-1)

print(cnt)


# 펜윅트리로 풀어보기

def make_fenwick(i, num): # 펜윅트리 만드는 함수
    while i <= g:         # 자신이 속해있는 인덱스들에 cost값 더해줌
        M[i] += num
        i += (i & -i)

def get_sum(i): # 펜윅트리에서 합 구하는 함수
    sum = 0
    while i > 0:
        sum += M[i]
        i -= (i & -i)
    return sum

g = int(input())
p = int(input())
M = [0 for _ in range(g+1)]

cnt = 0
for _ in range(p):
    n = int(input())
    if M[n] == 0:
        make_fenwick(n, 1)
        cnt += 1
    else:
        print(get_sum(n))
        if get_sum(n) < n:
            M[n] += 1
            cnt += 1
        else:
            break


print(cnt)