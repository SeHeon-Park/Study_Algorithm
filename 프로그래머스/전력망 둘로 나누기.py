from collections import defaultdict, deque

def solution(n, wires):
    ans = int(1e9)
    tree = defaultdict(list)
    for w in wires:
        tree[w[0]].append(w[1])
        tree[w[1]].append(w[0])

    for w in wires:
        visited = [0 for _ in range(n+1)]
        C = []
        for i in range(1, n+1):
            if visited[i]: continue
            visited[i] = 1
            cnt = 1
            Q = deque()
            Q.append(i)
            while Q:
                cur = Q.popleft()
                for target in tree[cur]:
                    if (cur, target) == (w[0], w[1]) or (cur, target) == (w[1], w[0]) or visited[target]: continue
                    cnt += 1
                    visited[target] = 1
                    Q.append(target)
            C.append(cnt)
        print(C)
        ans = min(ans, abs(C[0]-C[1]))

    return ans

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])