from itertools import permutations
import re

def operation(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


def solution(expression):
    answer = 0
    op = []
    op_type = []
    number = []
    word = ''
    # for e in expression:
    #     if any(e == i for i in ['+', '-', '*']):
    #         op.append(e)
    #         number.append(int(word))
    #         word = ''
    #         continue
    #     word += e
    # number.append(int(word))
    # temp1 = number.copy()
    # temp2 = op.copy()
    op = re.split('[0-9]+', expression)[1:-1]
    temp = op.copy()
    op_type = list(set(op))
    for i in list(permutations(op_type)):
        # number = temp1.copy()
        # op = temp2.copy()
        number = re.split('[*+-]', expression)  # 스플릿 활용하면 저 위에 지저분한 코드 생략 가능!
        number = list(map(int, number))
        op = temp.copy()
        for o in i:
            while o in op:  # 핵심! while True문 안써도 되네
                idx = op.index(o)
                number[idx] = operation(op[idx], number[idx], number[idx+1])
                del number[idx + 1]
                del op[idx]
        answer = max(answer, abs(number[0]))

    return answer