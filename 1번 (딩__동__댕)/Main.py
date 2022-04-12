from bisect import bisect_left, bisect_right

n = int(input())
A = []
count=0
for i in range(n):
    A.append(int(input()))

A.sort()  # 리스트를 정렬

for i in range(n-2):          
    for j in range(i+1, n-1):   # a,b 뽑기
        r = 3*A[j]-2*A[i]
        l = 2*A[j]-A[i]
        count += bisect_right(A[j+1:], r) - bisect_left(A[j+1:], l) # c가 될수 있는 개수 더해줌

print(count)

# 입력받은 값을 정렬을 하여 첫번째 조건을 만족 시킨다. 두번째 조건을 변형시키면 2b-a<=c<=3b-2a이다.
# 정렬된 리스트에서 a,b를 for문을 통해 뽑아주고 2b-a<=c<=3b-2a를 만족시키는 c를 이진탐색을 통해 뽑아준다.

# bisect_right(a, x)함수: 이진탐색을 하며 x값이 리스트a에 있으면 뒤의 위치를 반환한다. 
# bisect_left(a, x)함수: 이진탐색을 하며 x값이 리스트a에 있으면 해당 위치를 반환한다.
# 두 함수모두 a리스트에 x값이 없다면 오름차순에 들어갈 위치를 반환한다.
# 따라서 두 함수가 반환한 인덱스의 차는 c가 될 수 있는 개수를 의미한다.

# 수행시간 분석
# 두개의 for문에서 a,b를 뽑는데 T(n) = (n-2)+(n-3)+(n-4)...+1 ==>O(n^2)이고 이진탐색의 경우 항상 O(log(n))을 만족하므로 O(n^2logn)이다.