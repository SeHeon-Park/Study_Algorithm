- 트라이 알고리즘 적용 풀이

class Trie(object):
    def __init__(self):
        self.head = {}

    def insert(self, data):
        curr_node = self.head
        for d in data:
            if not d in curr_node:
                curr_node[d] = {}
            curr_node = curr_node[d]

    def print(self, curr, depth=0):
        keys = sorted(curr.keys())
        for k in keys:
            print("--" * depth + k)
            self.print(curr[k], depth+1)


import sys

n = int(input())
trie = Trie()
temp = []

for i in range(n):
    num, *string = sys.stdin.readline().rstrip().split()
    trie.insert(string)
trie.print(trie.head)


- 처음 푼 코드

import sys

n = int(input())
temp = []

for i in range(n):
    num, *string = sys.stdin.readline().rstrip().split()
    temp.append(string)

temp.sort()
k = "--"
for i in range(len(temp)):
    for j in range(len(temp[i])):
        if i == 0 and j == 0:
            print(temp[i][j])
            continue
        if i != 0 and len(temp[i-1])-1 >= j and temp[i][j] == temp[i-1][j]:
            continue
        t = k*j
        print(t+temp[i][j])