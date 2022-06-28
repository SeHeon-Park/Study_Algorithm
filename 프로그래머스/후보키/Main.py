from itertools import combinations

def check(result, t):
    for i in range(1, len(t) + 1):
        for c in combinations(t, i):
            if c in result:
                return False
    return True


def sum_s(s, t):
    word = ''
    for i in t:
        word += s[i]
    return word


def solution(relation):
    result = []
    temp = [i + 1 for i in range(-1, len(relation[0]) - 1)]
    for i in range(1, len(temp) + 1):
        for t in combinations(temp, i):
            if not check(result, t):
                continue
            print(result, t)
            part = []
            flag = 0
            for j in range(len(relation)):
                if sum_s(relation[j], t) in part:
                    flag = 1
                    break
                part.append(sum_s(relation[j], t))
            if flag == 0:
                result.append(t)

    return len(result)

- 다음 방법을 생각해보자

def is_powerset(parent, child):
    return (parent | child) == parent # or연산을 해서 원래랑 같다면 child는 parent의 부분집합!

비트연산으로 문제를 풀 경우 or(|)연산으로 최소성 연산을 수행 할 수 있다..