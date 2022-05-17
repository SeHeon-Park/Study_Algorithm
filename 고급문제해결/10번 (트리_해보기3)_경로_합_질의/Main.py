def set_preorder(temp, w):  # preorder리스트, ancestor_count리스트, cost리스트 채우기(재귀 사용)
    if len(temp) == 0:  # 리프노드면 return
        return
    for x in temp:  # 자식들을 돌며
        preorder.append(x)  # 자기 자신 채움
        ancestor_count.append(ancestor_sorted[x])  # 자신의 자식수도 채움
        path_sum.append(cost[x - 1] + w) # 지나온 weight값 저장
        w += cost[x - 1]
        set_preorder(dic[x][1:], w)  # 자신의 자식들로 다시 함수 호출
        w -= cost[x - 1]

def set_ancestor():  # 자식들의 수 채우는 함수(ancestor_sorted)
    for i in dic.keys():
        if i == 0:
            continue
        while i != 1:  # 트리를 거슬러 올라가며
            ancestor_sorted[dic[i][0]] += 1  # 부모노드의 자식 수 추가
            i = dic[i][0]  # 자신을 부모노드로 update

def set_diff():
    diff.append(path_sum[0])
    for i in range(1, n):
        diff.append(path_sum[i] - path_sum[i - 1])

def make_fenwick_plus(i, num):  # 펜윅트리 만드는 함수
    while i <= n:  # 자신이 속해있는 인덱스들에 cost값 더해줌
        diff_tree[i] += num
        i += (i & -i)

def make_fenwick_minus(i, num):  # 펜윅트리 만드는 함수
    while i <= n:  # 자신이 속해있는 인덱스들에 cost값 빼줌
        diff_tree[i] -= num
        i += (i & -i)

def get_sum(i):  # 펜윅트리에서 합 구하는 함수
    sum = 0
    while i >= 1:
        sum += diff_tree[i]
        i -= i & -i
    return sum

def query_sum(v):
    index = preorder.index(v)  # preorder에서 구하고자 하는 노드의 index
    print(get_sum(index + 1))  # 합 출력

def query_update(v, d):
    index = preorder.index(v)  # preorder에서 구하고자 하는 노드의 index
    make_fenwick_plus(index + 1, d)
    if index == 0: # 루트노드면 아무영향을 안끼침
        return
    if ancestor_count[index] != 0: # 자식이 있다면 자식들 다음 노드들에게 영향
        make_fenwick_minus(index + ancestor_count[index] + 2, d)
    if ancestor_count[index] == 0: # 자식이 없다면 자신 다음 노드들에게 영향
        make_fenwick_minus(index + 2, d)


n, q = map(int, input().split())
cost = [int(x) for x in input().split()]  # 1~n까지 cost
path_sum = [cost[0]]  # preorder로 정렬된 노드순대로 지나온 cost값
preorder = [1]  # preorder리스트
dic = {1: [0]}  # key: 자신 노드, value: [부모노드, 자식노드들]
ancestor_sorted = [0 for _ in range(n + 1)]  # 1~n까지 자식의 수
ancestor_count = [n - 1]  # preorder로 정렬된 노드 순대로 자식의 수
diff = []
diff_tree = [0 for _ in range(n + 1)]  # diff배열에 대해 fenwick트리를 구성

for i in range(n - 1):  # (수행 시간) n-1만큼의 시간
    p, c = map(int, input().split())
    dic[p].append(c)  # 자식 채우기
    dic[c] = [p]  # 부모 채우기

set_ancestor()  # (수행 시간) 모든노드에 대해서 트리를 거슬러 올라가므로: 최악의 경우 n^2만큼의 시간
set_preorder(dic[1][1:], cost[0])  # (수행 시간) 모든 노드를 거쳐가므로: n만큼의 시간
set_diff()  # n-1의 시간

for i in range(0, n):  # (수행 시간) 펜윅트리 구성: nlogn만큼의 시간
    make_fenwick_plus(i + 1, diff[i])

for i in range(q):  # (수행 시간) q만큼의 시간
    query = input().split()
    if query[0] == 'sum':
        query_sum(int(query[1]))  # (수행 시간) 펜윅트리의 sum: logn만큼의 시간
    else:
        query_update(int(query[1]), int(query[2]))  # (수행 시간) 펜윅트리의 update: logn만큼의 시간

# dictionary에 key: 자신 노드, value: [부모노드, 자식노드들] 식으로 구성을 하여 활용을 하였다.
# preorder순으로 구성된 노드 리스트, preorder순으로 구성된 자식의 수 리스트, preorder순으로 구성된 지나온 cost값 리스트, diff리스트에 대한 펜윅트리 구하여 활용하였다.

# 1. query_sum
# - preorder리스트에서 구하고자 하는 노드의 index을 구하였고, fenwick_tree를 활용하여 루트노드부터 합을 구하였다

# 2. query_update
# - preorder리스트에서 구하고자 하는 노드의 index을 구하였다.
# - 루트노드인 경우 아무런 영향이 없으므로 그냥 return하였다.
# - 자식이 있다면 diff_fenwick_tree[자신의 자식을 제외하고 그 다음 노드의 index]값에서 d값을 빼주었다.
# - 자식이 없다면 diff_fenwick_tree[자신의 다음 노드의 index]값에서 d값을 빼주었다.

# 수행시간
# (52줄부터 주석 참고)
# 따라서 수행시간은 T(n)= (n-1) + n^2 + n + nlogn + 2qlogn 이고 결국 최악의 경우 O(n)=n^2이다.(q가 n보다 커질수 있음)


