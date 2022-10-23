for t in range(10):
    M=[]
    case = int(input())
    for _ in range(100):
        M.append(list(map(int, input().split())))
    x = M[-1].index(2)
    h = 99
    while h >= 0:
        h -= 1
        if x-1 >= 0 and M[h][x-1] == 1:
            while M[h][x] != 0:
                if x == 0:
                    break
                x -= 1
            if x != 0:
                x += 1
        elif x+1 <= 99 and M[h][x+1] == 1:
            while M[h][x] != 0:
                if x == 99:
                    break
                x += 1
            if x != 99:
                x -= 1
    print("#{} {}".format(t+1, x))
