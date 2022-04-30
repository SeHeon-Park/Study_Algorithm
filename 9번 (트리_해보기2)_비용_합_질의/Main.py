def set_preorder(temp):  # preorder리스트, ancestor_count리스트, cost리스트 채우기(재귀 사용)
    if len(temp) == 0:   # 리프노드면 return
        return
    for x in temp:         # 자식들을 돌며
        preorder.append(x) # 자기 자신 채움
        ancestor_count.append(ancestor_sorted[x]) # 자신의 자식수도 채움 
        cost.append(first_cost[x - 1])            # cost도 채움
        set_preorder(dic[x][1:])                  # 자신의 자식들로 다시 함수 호출

def set_ancestor(): # 자식들의 수 채우는 함수(ancestor_sorted)
    for i in dic.keys():
        if i == 0:
            continue
        while i != 1:                       # 트리를 거슬러 올라가며
            ancestor_sorted[dic[i][0]] += 1 # 부모노드의 자식 수 추가
            i = dic[i][0]                   # 자신을 부모노드로 update

def make_fenwick(i, num): # 펜윅트리 만드는 함수
    while i <= n:         # 자신이 속해있는 인덱스들에 cost값 더해줌
        cost_tree[i] += num
        i += (i & -i)

def get_sum(i): # 펜윅트리에서 합 구하는 함수
    sum = 0
    while i>=1:
        sum += cost_tree[i]
        i -= i & -i
    return sum

def query_subtree(i):
    index = preorder.index(i) # preorder에서 구하고자 하는 노드의 index
    left = index+1              # 펜윅트리에서의 왼쪽 범위
    right = left + ancestor_count[index]  # 펜윅트리에서의 오른쪽 범위(왼쪽 범위에서 자식의 수 만큼 더함)    
    print(get_sum(right)-get_sum(left-1)) # 구간합 출력

def query_update(i, num): 
    index = preorder.index(i)  # preorder에서 구하고자 하는 노드의 index
    make_fenwick(index+1, num) # update!



n, q = map(int, input().split())
first_cost = [int(x) for x in input().split()]  # 1~n까지 cost
cost = [first_cost[0]] # preorder로 정렬된 노드순대로 cost
preorder = [1] # preorder리스트
dic = {1: [0]} # key: 자신 노드, value: [부모노드, 자식노드들]
ancestor_sorted = [0 for _ in range(n + 1)] # 1~n까지 자식의 수
ancestor_count = [n - 1] # preorder로 정렬된 노드 순대로 자식의 수
cost_tree = [0 for _ in range(n + 1)] # cost배열에 대해 fenwick트리를 구성


for i in range(n - 1):                # (수행 시간) n-1만큼의 시간
    p, c = map(int, input().split())
    dic[p].append(c) # 자식 채우기
    dic[c] = [p]     # 부모 채우기

set_ancestor()                        # (수행 시간) 모든노드에 대해서 트리를 거슬러 올라가므로: 최악의 경우 n^2만큼의 시간
set_preorder(dic[1][1:])              # (수행 시간) 모든 노드를 거쳐가므로: n만큼의 시간

for i in range(0, n):                 # (수행 시간) 펜윅트리 구성: nlogn만큼의 시간
    make_fenwick(i + 1, cost[i])

for i in range(q):	                  # (수행 시간) q만큼의 시간
    query = input().split()
    if query[0] == 'subtree':
        query_subtree(int(query[1]))  # (수행 시간) 펜윅트리의 sum: logn만큼의 시간
    else:
        query_update(int(query[1]), int(query[2]))  # (수행 시간) 펜윅트리의 update: logn만큼의 시간


# dictionary에 key: 자신 노드, value: [부모노드, 자식노드들] 식으로 구성을 하여 활용을 하였다. 
# preorder순으로 구성된 노드 리스트, preorder순으로 구성된 자식의 수 리스트, preorder순으로 구성된 cost리스트, cost리스트에 대한 펜윅트리 구하여 활용하였다.

# 1. query_subtree
# - preorder리스트에서 구하고자 하는 노드의 index을 구하였고, 그 index를 활용해 left, right 범위를 구하였다.(right=left+자신의 자식의 수)
# - 펜윅트리를 활용해 구간합을 구하였다.

# 2. query_update
# - preorder리스트에서 구하고자 하는 노드의 index을 구하였다.
# - update같은 경우 결국 자신의 원래 cost값에서 추가로 num만큼 더해주기만 하면 되어 make_fenwick함수를 호출하면 된다.

# 수행시간
# (52줄부터 주석 참고)
# 따라서 수행시간은 T(n)= (n-1) + n^2 + n + nlogn + 2qlogn 이고, 결국 최악의 경우 O(n)=n^2이다.


