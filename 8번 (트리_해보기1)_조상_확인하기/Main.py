def query_ancestor(u, v):
    if u == 1 or u == v: return True  # u가1이거나 u, v가 같은경우는 항상 True이다
    if dic[u][0] >= dic[v][0]: return False # u의 level이 v의 level보다 크거나 같으면 항상 False이다.
    level = dic[v][0]
    while level > dic[u][0]: # 트리를 거슬러 올라가면서 부모를 찾는다
        v = dic[v][1] # v를 update!
        if v == u: # 부모를 찾았다면 True
            return True
        level = dic[v][0]
    return False

count = 0
dic = {1: [0]} # 루트노드인 1 저장
n, q = map(int, input().split())
for i in range(n-1):
    p, c = map(int, input().split())
    dic[c] = [dic[p][0]+1, p] # dic의 value값에 노드의 level과 부모노드 저장

for i in range(q):
    u, v = map(int, input().split())
    if query_ancestor(u, v): # True이면 count+=1
        count += 1

print(count)

# dictionary에 key값에는 자기자신 노드를, value값에는 자신의 level과 부모노드를 저장한다. {자신노드 : [level, 부모노드]}
# query_ancestor함수에서 v부터 u의 level까지 거슬러 올라가며 u를 찾는다

# 수행시간
# 1. dic에 노드의 정보를 저장하는데 n-1만큼 시간이 걸린다.
# 2. q개의 query를 돌며 v에서부터 올라가며 부모를 찾는다. 여기서 최악의 경우는 루트노드부터 리프노트까지 한노드씩 쭉 이어지는 경우이다. 따라서 qn만큼 시간이 걸린다.
# 따라서 수행시간은 T(n)=n-1+qn이고 상수를 제외하고 O(n)=(q+1)n만큼 시간이 걸린다.
