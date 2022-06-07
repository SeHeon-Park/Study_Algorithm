from itertools import combinations # 외우기
import math

def combinations_list(order, c):
    board = []
    a = list(combinations(order, c)) # 튜플로 저장됨
    for j in a:
        word = ''
        for k in j:
            word += k
        board.append(word)
    return board

def solution(orders, course):
    answer = []
    for i in range(len(orders)):
        orders[i] = sorted(orders[i]) # 문자열 자체를 정렬 할때는 sorted("문자열")
    for c in course:
        board = combinations_list(orders[0], c)
        menu = {}
        for o in range(1, len(orders)):
            l = combinations_list(orders[o], c)
            for i in range(len(l)):
                if l[i] in board:
                    if l[i] in menu:
                        menu[l[i]] = menu[l[i]] + 1
                    else:
                        menu[l[i]] = 1
                else:
                    board.append(l[i])

        m = -math.inf
        for i in menu.values():
            m = max(m, i)
        for s in menu: # s에 key값 나옴
            if menu[s] == m:
                answer.append(s)
    answer.sort() # 문자 기준으로 리스트 정렬
    return answer
