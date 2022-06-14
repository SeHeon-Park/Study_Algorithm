import re
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left, bisect_right


def solution(info, query):
    answer = []
    dic = defaultdict(list)  # List가지고 있는데 dic(중요!) (dic['a'].append(1)했을때 dic에 'a'가 없어도 오류 안뜸!)
    score = []
    for i in range(len(info)):
        info[i] = re.split("\s", info[i])  # 공백에 따라 나누기
        for k in range(1, 5):
            for j in combinations(info[i][:-1], k):  # 반복없는 조합
                word = ''
                for p in j:
                    word += p
                dic[word].append(int(info[i][-1]))
        score.append(int(info[i][-1]))
    for v in dic.values():
        v.sort()
    score.sort()


    for q in query:
        q = q.replace('and', '').replace('-', '').replace(' ', '')
        number = re.sub(r'[^0-9]', '', q)  # 숫자만 추출
        q = re.sub(r'[0-9]', '', q)        # 숫자만 없애기
        if len(q) == 0:
            answer.append(len(info) - bisect_left(score, int(number)))
            continue
        n = bisect_left(dic[q], int(number))
        answer.append(len(dic[q]) - n)
    return answer


## 효율성 때문에 고생, 이진탐색으로 줄일 수 있다..
# bisect_left, bisect_right 코드 외우자!

# 이분 탐색이 '원하는 값을 찾는 과정'
# Lower Bound는 '원하는 값 이상이 처음 나오는 위치를 찾는 과정' (bisect_left) => 리스트에 값이 같은 경우가 있다면 가장 왼쪽것 반환
# Upper Bound는 '원하는 값을 초과한 값이 처음 나오는 위치를 찾는 과정' (bisect_right)


# left와 right의 차이

# left
# if a[mid] < x: lo = mid+1
# else: hi = mid

# right
# if a[mid] > x: hi = mid
# else: lo = mid + 1
