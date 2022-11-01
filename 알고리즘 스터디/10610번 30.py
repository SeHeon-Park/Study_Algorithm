n = input()
M = ''.join(sorted(n, reverse=True))
if eval(M+"%30"):
    print(-1)
else:
    print(M)