n = int(input())
A = [int(x) for x in input().split()]
dic = {int(x):0 for x in A}
l = n/2

for a in A:
    dic[a] = dic[a] + 1

m = max(dic.values())

if m > l:
    for x in dic.keys():
        if dic[x] == m:
            print(x)
else:
    print(-1)


# 딕셔너리를 사용해 리스트에서 후보들이 나올때마다 해당 후보를 key값으로 두고 value값을 1씩 더해주었다.
# max함수를 사용해 value값이 가장 큰, 즉 가장 투표를 많이 받은 후보를 뽑아 주었다.
# 그 투표수가 limit를 넘는다면 딕셔너리에서 후보를 찾아 출력, 넘지 않는다면 -1출력 

# 수행시간
# 처음 딕셔너리에 후보를 넣을때 n, 딕셔너리에서 max함수 사용 (최악)n, 마지막 후보를 찾을때 (최악)n번 해서 상수제외 T(n) = 3n정도 걸리고 빅오는 O(n)이다. 
# n명의 시민이 각자 다른 후보를 뽑는 최악의 경우가 아니면 리스트로 돌리는 것보다 비교적 빠르게 돌릴수 있다. 
