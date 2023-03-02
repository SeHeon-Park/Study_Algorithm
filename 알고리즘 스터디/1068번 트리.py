import sys
from collections import defaultdict
input = sys.stdin.readline

def leaf_cnt(node):
    global cnt_l
    if node not in dic.keys():
        cnt_l += 1
        return
    for n in dic[node]:
        leaf_cnt(n)
    return


def remove(node):
    global cnt_r
    if node not in dic.keys():
        cnt_r += 1
        return
    for n in dic[node]:
        remove(n)
    return


n = int(input())
A = [int(x) for x in input().split()]
dic = defaultdict(list)

for i in range(n):
    dic[A[i]].append(i)


cnt_l = 0
cnt_r = 0
leaf_cnt(-1)
m = int(input())
remove(m)
if A[m] != -1 and len(dic[A[m]]) == 1:
    cnt_l += 1
print(cnt_l-cnt_r)