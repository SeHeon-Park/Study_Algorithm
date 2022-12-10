def solution(info, edges):
    visited = [0 for _ in range(len(info))]
    visited[0] = 1
    ans = []
    def dfs(sheep, wolf):
        if sheep > wolf:
            ans.append(sheep)
        else:
            return
        for p, s in edges:
            if visited[p] and not visited[s]:
                visited[s] = 1
                if info[s]:
                    dfs(sheep, wolf+1)
                else:
                    dfs(sheep+1, wolf)
                visited[s] = 0
        return
    dfs(1, 0)
    return max(ans)