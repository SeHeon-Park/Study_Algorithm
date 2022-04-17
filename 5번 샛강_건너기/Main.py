import math

L, n, k = map(int, input().split())
A = [int(x) for x in input().split()]
A.append(L) # 마지막 도착지 거리 계산

def findK(L, k):
	l = 1
	r = L
	while l<=r:
		m =(l+r)//2 # m보다 작으면 delete!
		delete = 0 # 제거된 돌 개수
		current_loc = 0 # 현재 위치
		distance = math.inf  # 최소거리 check 
		for a in range(n+1): # 첫 돌부터 m과 비교하여 작으면 delete, 크거나 같으면 현재위치를 해당돌로 옮긴다.
			if A[a]-current_loc < m:
				delete += 1
			else:
				distance = min(distance, A[a]-current_loc) # 해당 m단계에서 바위 간격이 최소값이면 update!
				current_loc = A[a]
			
		if delete > k: # 제거된 돌개수가 기준값보다 크다면
			r = m-1 # m을 줄여서 다시 확인
		else: # 제거된 돌개수가 기준값보다 작거나 같다면
			l = m+1 # m을 늘려서 다시 확인
							# 제거된 돌개수가 같아도 최대값이 아닐수도 있기 때문에 다시 확인
			ans = distance # ans을 update
	return ans


print(findK(L, k))

# 조건을 만족하는 바위사이의 간격이 1과 L사이 이므로 1을 left, L을 right로 지정해 이진탐색을 통해 해결하였다.
# 첫 바위부터 시작해 현재위치에서 바위사이의 간격이 m보다 작으면 delete, m보다 크면 돌을 살리고 현재위치를 해당돌로 옮겨주었다.
# 마지막 바위까지 돌았을때 제거된 돌의 개수와 k와 비교를 하여 제거된 돌의 개수가 k보다 크면 m을 줄여주고 k보다 작거나 같으면 m을 늘려주었다.(제거된 돌의개수와 k값이 같아도 최대값을 구해야되기 때문에 다시 확인한다.)

#수행시간
# 1과 L사이를 이진탐색하는데 logL의 시간이 걸리고, 이진탐색을 하며 첫돌부터 마지막 돌까지 n+1번 돈다
# 따라서 O(logL * n)정도의 시간이 걸린다.
