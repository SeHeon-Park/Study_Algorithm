T = int(input())

def dfs(cnt, idx):
    global ans
    if cnt > k:
        return
    if cnt == k:
        ans += 1
        return
    for i in range(idx, n):
        dfs(cnt+A[i], i+1)
    return

for t in range(T):
    ans = 0
    n, k = map(int, input().split())
    A = [int(x) for x in input().split()]
    dfs(0, 0)
    print("#{} {}".format(t+1, ans))
