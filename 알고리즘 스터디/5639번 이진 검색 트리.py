import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur):
    if cur not in dic.keys():
        print(cur)
        return
    for v in dic[cur]:
        dfs(v)
    print(cur)
    return

M = [10**6]
dic = defaultdict(list)
while True:
    try:
        n = int(input())
        if M[-1] < n:
            while True:
                if M[-1] < n:
                    a = M.pop()
                    continue
                else:
                    dic[a].append(n)
                    M.append(n)
                    break
        else:
            dic[M[-1]].append(n)
            M.append(n)
    except:
        break

root = dic[10**6][0]
dfs(root)
