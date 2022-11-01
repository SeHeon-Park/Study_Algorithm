## 딕셔너리 풀이
T = int(input())
for _ in range(T):
    n = int(input())
    A, dic = [], {}
    flag = 0
    for _ in range(n):
        a = input()
        A.append(a)
        dic[a] = len(a)
    for a in A:
        if flag:
            break
        temp = ''
        for i in a:
            temp += i
            if temp in dic.keys() and dic[temp] != len(a):
                flag = 1
                break
    if not flag:
        print("YES")
    else:
        print("NO")

## sort 풀이
T = int(input())
for _ in range(T):
    n = int(input())
    A = []
    flag = 0
    for _ in range(n):
        A.append(input())
    A.sort()
    for i in range(len(A)-1):
        if flag:
            break
        for j in range(i+1, len(A)):
            if A[i][0] != A[j][0] or len(A[i]) >= len(A[j]):
                break
            if A[i] in A[j]:
                flag = 1
                break
    if not flag:
        print("YES")
    else:
        print("NO")
