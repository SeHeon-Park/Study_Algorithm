import sys
input = sys.stdin.readline

# 합, min, max, gcd 등 전부다 가능
def merge(left, right):
    return left+right

# 트리 만들기
def make_Tree(idx, left, right):
    # 리프 노드 도달
    if left == right:
        tree[idx] = M[left]
        return tree[idx]
    mid = (left+right)//2
    left_val = make_Tree(2*idx, left, mid)
    right_val = make_Tree(2*idx+1, mid+1, right)
    tree[idx] = merge(left_val, right_val)
    return tree[idx]


# 구간합 구하기
def query_rec(left_idx, right_idx, idx, left, right):
    # 범위 안에 있으면 그냥 반환
    if left >= left_idx and right <= right_idx:
        return tree[idx]
    # 범위 안에 없으면 0 반환
    if right < left_idx or left > right_idx:
        return 0
    mid = (left+right)//2
    left_val = query_rec(left_idx, right_idx, idx*2, left, mid)
    right_val = query_rec(left_idx, right_idx, idx*2+1, mid+1, right)
    return merge(left_val, right_val)

def query(left_idx, right_idx):
    return query_rec(left_idx, right_idx, 1, 0, n-1)


# update
def update_rec(u_idx, val, idx, left, right):
    # u_idx가 범위 안에 없으면 update 암함
    if u_idx > right or u_idx < left:
        return tree[idx]
    # u_idx를 찾으면 update
    if left == right:
        tree[idx] = val
        return tree[idx]
    mid = (left+right)//2
    left_val = update_rec(u_idx, val, idx*2, left, mid)
    right_val = update_rec(u_idx, val, idx*2+1, mid+1, right)
    tree[idx] = merge(left_val, right_val)
    return tree[idx]

def update(u_idx, val):
    return update_rec(u_idx, val, 1, 0, n-1)


n, m, k = map(int, input().split())
tree = [0 for _ in range(n * 4)]
M = []

for i in range(n):
    M.append(int(input()))

make_Tree(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b-1, c)
    else:
        print(query(b-1, c-1))
