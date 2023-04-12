import sys
input = sys.stdin.readline

def merge(left, right):
    return left+right

def make_Tree(idx, left, right):
    if left == right:
        tree[idx] = M[left]
        return tree[idx]
    mid = (left+right)//2
    left_val = make_Tree(2*idx, left, mid)
    right_val = make_Tree(2*idx+1, mid+1, right)
    tree[idx] = merge(left_val, right_val)
    return tree[idx]


def query_rec(left_idx, right_idx, idx, left, right):
    if left >= left_idx and right <= right_idx:
        return tree[idx]
    if right < left_idx or left > right_idx:
        return 0
    mid = (left+right)//2
    left_val = query_rec(left_idx, right_idx, idx*2, left, mid)
    right_val = query_rec(left_idx, right_idx, idx*2+1, mid+1, right)
    return merge(left_val, right_val)

def query(left_idx, right_idx):
    return query_rec(left_idx, right_idx, 1, 0, n-1)


def update_rec(u_idx, val, idx, left, right):
    if u_idx > right or u_idx < left:
        return tree[idx]
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
