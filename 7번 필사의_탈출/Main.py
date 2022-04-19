u = int(input())
U = [int(x) for x in input().split()]
minimum = min(U)

m = int(input())
M = [int(x) for x in input().split()]
minimum = min(minimum, min(M))

l = int(input())
L = [int(x) for x in input().split()]
minimum = min(minimum, min(L))

# 음수를 없애기 위해 minimum을 더해줌
if minimum < 0:
	for i in range(u):
		U[i] += abs(minimum)+1
	for j in range(m):
		M[j] += abs(minimum)+1
	for k in range(l):
		L[k] += abs(minimum)+1

index = 0
M_max = max(M) # M에서 최대값 저장
M_zero = [0] * (M_max+1) # M_max만큼 0으로 채움

for x in M: # 구멍인 index를 1로 채움
    M_zero[x] = 1

count = 0

for i in range(u):
    for j in range(l):
        if U[i]%2 != L[j]%2: # (홀, 홀), (짝, 짝)형태여야 함
            continue
        temp = (U[i]+L[j])//2
        if temp <= M_max and M_zero[temp] == 1: # 구멍인 인덱스면 count+=1
            count += 1

print(count)


# 가운데인 M을 좌표에 맞게 index를 1로 채워 놓으면 M[(l+u)//2]가 1인 부분이 직선인 경우 이므로 l,u루프를 돌며 M[(l+u)//2]가 1인 경우 count를 늘려주었다.

# 시간복잡도
# - 음수를 없애는데 -> u+m+l
# 3. max(M) -> m
# 4. 구멍인 인덱스 채우는데 -> m 
# 5. u, l 이중 for문 -> ul
# 따라서 T(n) = ul+u+3m+l