import sys
input = sys.stdin.readline

def get_height(target):
    h = 0
    while True:
        if target == 1:
            break
        target = dic[target]
        h += 1
    return h

n = int(input())
info = input()[:-1]
info = list(int(m) for m in info)
dic = {}

x, y = map(int, input().split())
D = []

num = 1
parent = "root"
for i in range(len(info)):
    if info[i] == 0:
        D.append(num)
        dic[num] = parent
        parent = num
        num += 1
    else:
        D.append(parent)
        parent = dic[parent]

X, Y = D[x - 1], D[y - 1]
x_height = get_height(X)
y_height = get_height(Y)

if x_height < y_height:
    X, Y = Y, X
    x_height, y_height = y_height, x_height

while x_height != y_height:
    X = dic[X]
    x_height -= 1

while X != Y:
    X = dic[X]
    Y = dic[Y]

for i in range(len(D)):
    if D[i] == X:
        print(i+1, end=" ")