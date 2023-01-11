def solution(users, emoticons):
    ans = []
    original = list(a[:] for a in users)
    visited = [0 for _ in range(len(users))]

    def dfs(idx, cnt, price, users, visited):
        if idx == len(emoticons):
            ans.append([cnt, price])
            return

        for d in [0.1, 0.2, 0.3, 0.4]:
            temp_users = list(a[:] for a in users)
            temp_visited = list(v for v in visited)
            temp_price = price
            temp_cnt = cnt
            discount = emoticons[idx] - int(emoticons[idx]*d)
            for u in range(len(users)):
                if visited[u] == 1:
                    continue
                if users[u][0] <= d*100:
                    p = users[u][1]-discount
                    if p <= 0:
                        visited[u] = 1
                        cnt += 1
                        price -= (original[u][1] - users[u][1])
                    else:
                        price += discount
                    users[u][1] = p

            dfs(idx+1, cnt, price, users, visited)

            users = list(a[:] for a in temp_users)
            visited = list(v for v in temp_visited)
            price = temp_price
            cnt = temp_cnt
        return
    dfs(0, 0, 0, users, visited)
    ans.sort(key=lambda x:(-x[0], -x[1]))
    return ans[0]