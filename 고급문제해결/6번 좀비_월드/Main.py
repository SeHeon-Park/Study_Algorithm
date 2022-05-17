from collections import deque

n, L ,k = map(int, input().split())
A, B = [], [] # A에는 좀비들의 위치 저장, B에는 좀비들의 아이디값 저장
ans_left, ans_right = [], [] # 좀비들이 절벽에서 떨어지는 시간들 저장(ans_left는 마지막모습이 -인 좀비들, ans_right는 마지막모습이 +인 좀비들)
deq = deque()
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
		
def pm_count(): # minus와 plus의 개수를 파악하여 return
    minus, plus  = 0, 0 # minus, plus인 좀비들의 개수
    minus_count, plus_count = 0, 0 # 충돌하지 않고 바로 떨어지는 좀비들의 개수
    last_plus = len(B)-1
    while B[minus_count] < 0:
        minus_count += 1
        if minus_count == len(B): # 전부다 충돌하지 않고 떨어지는 좀비라면
            break
    while B[last_plus] > 0:
        plus_count += 1
        last_plus -= 1
        if plus_count == len(B): # 전부다 충돌하지 않고 떨어지는 좀비라면
            break
    for b in B:
        if b<0:
            minus += 1
        else:
            plus += 1
    return minus_count, plus_count, minus, plus

first_minus, last_plus, minus, plus = pm_count()


def find_time():
    for fm in range(first_minus): # 바로 떨어지는 좀비들 시간 저장(양변 둘다 저장)
        ans_left.append(A[fm])
    for lp in range(last_plus):
        ans_right.append(L-A[len(A)-1-lp])

    count = first_minus  # minus 좀비 count
    index = first_minus  # deq에 들어가는 좀비 인덱스
    if minus != first_minus: # 절벽에 떨어지는 좀비밖에 없다면 연산 할 필요없음
        while minus != count or index < len(B)-1: # minus만큼 진행을 함
            deq.append(A[index]) # 좀비들을 deq에 저장
            if B[index] < 0: # 처음으로 -인 좀비와 마주치면
                deq.popleft() # 해당 좀비를 제거해주며
                ans_left.append(A[index]) # 시간 저장
                count += 1 # count 증가
            index += 1


    count = last_plus
    index = len(B)-1-last_plus
    if plus != last_plus:
        while plus != count or index > 0:
            deq.append(A[index])
            if B[index] > 0: #처음으로 +인 좀비와 마주치면
                deq.popleft() 
                ans_right.append(L-A[index])
                count += 1
            index -= 1

find_time()

for i in range(len(ans_right)-1, -1, -1): # 인덱스가 맞게끔 ans_left로 합침
    ans_left.append(ans_right[i])

count = 0
l, r = 0, len(ans_left)-1
ans_index = 0 # k번째로 떨어지는 좀비 인덱스

while count != k: 
	# k번째로 떨어지는 좀비 찾기, 무조건 외곽부터 떨어지므로 양변으로 비교
    if ans_left[l] < ans_left[r]: 
        ans_index = l
        l += 1
        count += 1
    elif ans_left[l] > ans_left[r]:
        ans_index = r
        r -= 1
        count += 1
    else: # 시간이 같다면
        if B[l] < B[r]: # 아이디가 더 작은 좀비부터 떨어짐 
            ans_index = l
            l += 1
            count += 1
        else:
            ans_index = r
            r -= 1
            count += 1

print(B[ans_index])

# 결국 좀비들은 +/- 개수에 따라 왼쪽에 떨어질지 오른쪽에 떨어질지 결정이된다.
# 예를 들어 아이디가 -1/+2/+3/-4/-5/-6/+7(첫 모습) 인경우 -는 4개가 있고, +는 3개가 있어 마지막 모습은 -1/-2/-3/-4/+5/+6/+7(마지막 모습) 형태가 된다. 
# 여기서 1번좀비와, 7번 좀비 같은 경우 아무 충돌 없이 바로 절벽으로 가므로 시간이 바로 정해진다. (절벽에서 떨어지는 시간으로 계산하지 않고 절벽까지 가는 시간으로 계산함 => k번째로 떨어지는 좀비를 구하는것이므로 결국 답은 똑같음)
# 나머지 마지막 모습에서 아이디가 -인 좀비 3마리(-2, -3, -4)와 아이디가 +인 좀비 2마리(+6, +7)는 각각 다음과같은 규칙을 가지고있다.

# deque를 이용하여 마지막모습이 -좀비같은 경우 (첫 모습)에서 처음으로 deque에 들어온 -좀비의 인덱스 만큼 시간이 걸린다. 예를 들어 2번 좀비는 4만큼의 시간이 걸리고 3번좀비는 5만큼의 시간이 걸리고 4번좀비는 6만큼의 시간이 걸린다.. 
# 이유는 2번 좀비를 예로들면 결국 (자기 인덱스인 2만큼의 시간) + (3번과 4번이 만나는 시간*2) + (2번과 3번이 만나는 시간*2) => (처음으로 -인 좀비를 만나는 시간: 2)+((첫 모습)자기 위치에서 절벽(0)까지 거리: 2) = 4이기 때문이다. 나머지도 마찬가지다.
# 마지막 모습이 +좀비같은 경우도 결국 똑같은 원리로 (처음으로 +인 좀비를 만나는 시간) + ((첫 모습)자기 위치에서 절벽(L)까지 거리) 만큼 걸린다.(반대서부터 시작함)
# 위 과정은 deque를 통하여 구현하였다.

# 수행시간
# 1, 좀비들의 위치와 아이디를 저장하는데 n시간 걸린다
# 2, pm_count함수와 find_time함수에서 최악의 경우가 절벽에 떨어지는 좀비밖에 없는 경우와 절벽에서 떨어지는 좀비가 한마리도 없는경우가 있는데 각각 2n+n과 n+2n으로 결국 3n시간이 걸린다 
# 4, ans_left와 ans_right 합치는데 최악의 경우 n시간이 걸린다.
# 5, k번째로 떨어지는 좀비를 찾은데 n시간이 걸린다.
# 따라서 T(n) = n + 3n + n + n = 6n으로 결국 O(n)시간이 걸린다.
