import sys
input = sys.stdin.readline

def check():
    for i in range(len(b)):
        if Q[len(Q)-1-i] != b[len(b)-1-i]:
            return False
    return True

S = input()[:-1]
b = input()[:-1]
Q = []

for s in S:
    Q.append(s)
    if s == b[-1] and check():
        for i in range(len(b)):
            Q.pop()

if Q:
    for q in Q:
        print(q, end="")
else:
    print("FRULA")