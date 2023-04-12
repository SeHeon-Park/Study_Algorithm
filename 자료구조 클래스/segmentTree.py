n = int(input())
T = [int(x) for x in range(n*4)]

def merge(left, right):
    return left+right

# 트리 만들기
def build(node, node_left, node_right):
    if node_left == node_right:
        T[node] = T[node_left]
        return T[node]

    mid = (node_left + node_right) // 2
    left_val = build(node * 2, node_left, mid)
    right_val = build(node * 2 + 1, mid + 1, node_right)
    T[node] = merge(left_val, right_val)
    return T[node]


# 구간합 구하기
def query_rec(left, right, node, node_left, node_right):
    # 겹처면 한번더 내려가고, 안겹치면 0을 반환
    if right < node_left or node_right < left:
        return 0
    if left <= node_left and node_right <= right:
        return T[node]
    mid = (node_left+node_right)//2
    return merge(query_rec(left, right, node*2, node_left, mid),
                 query_rec(left, right, node*2+1, mid+1, node_right))

def query(left, right):
    return query_rec(left, right, 1, 0, n-1)


# update
def update_rec(idx, val, node, node_left, node_right):
    # 범위를 벗어나면 그대로 값 반환
    if idx < node_left or node_right < idx:
        return T[node]
    # 업데이트할 node 찾았으면 update!
    if node_left == node_right:
        T[node] = val
        return T[node]
    # 내려가기
    mid = (node_left + node_right) // 2
    left_val = update_rec(idx, val, node*2, node_left, mid)
    right_val = update_rec(idx, val, node*2+1, mid+1, node_right)

    T[node] = merge(left_val, right_val)
    return T[node]

def update(idx, val):
    return update_rec(idx, val, 1, 0, n-1)


# update 여러개 (별차이 없음, 안좋음 -> lazy propagation 사용해야함)
def update_range_rec(left, right, val, node, node_left, node_right):
    # 범위를 벗어나면 그대로 값 반환
    if right < node_left or node_right < left:
        return T[node]
    # 업데이트할 node 찾았으면 update!
    if node_left == node_right:
        T[node] = val
        return T[node]
    # 내려가기
    mid = (node_left + node_right) // 2
    left_val = update_rec(left, right, val, node * 2, node_left, mid)
    right_val = update_rec(left, right, val, node * 2 + 1, mid + 1, node_right)

    T[node] = merge(left_val, right_val)
    return T[node]


def update_range(left, right, val):
    return update_range_rec(left, right, val, 1, 0, n - 1)


build(1, 0, n-1)
print(query(2, 5))
