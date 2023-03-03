import sys
input = sys.stdin.readline

def recursive(p, o):
    if len(p) == 0:
        return
    if len(p) == 1:
        ans.append(p[0])
        S.add(p[0])
        return
    if p[0] not in S:
        # root 찾기
        for i in range(len(o)):
            if o[i] == p[0]:
                break
        # 왼쪽 자식들
        recursive(p[1:i+1], o[:i])
        # 오른쪽 자식들
        recursive(p[i+1:], o[i+1:])
        S.add(p[0])
        # 마지막에 중간
        ans.append(p[0])


T = int(input())
for t in range(T):
    n = int(input())
    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]
    root = preorder[0]
    S = set()
    ans = []
    # 좌 우 중
    recursive(preorder, inorder)
    print(*ans)

