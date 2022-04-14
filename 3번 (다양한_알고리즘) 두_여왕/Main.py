def diagonal(i, j):   # 대각선의 개수를 구하는 함수
    c, k = i, j
    p = 0
    while c<n-1 and k<n-1:  # 행+1, 열+1 대각선인 경우
        c+=1
        k+=1
        p+=1
    while i<n-1 and j>0:  # 행-1, 열+1 대각선인 경우
        i+=1
        j-=1
        p+=1
    return p

def even_Nqueen():  # n이 짝수일때 쌍의 개수 반환 함수
    count = 0
    for i in range(n - 1): # 행(맨마지막 행은 첫번째 퀸이 올수 없음)
        for j in range(n//2): # 열(n//2만큼만 루프돌아주고 2배주면 됨)
            count += (n - 1 - i) * n - (n - 1 - i + diagonal(i, j)) # 두번째 퀸이 위치할 수 있는 개수: (첫퀸 제외 나머지행)*n - (행-대각선)
    return 2*count 

def odd_Nqueen():  # n이 홀수 일때 쌍의 개수 반환 함수
    count = 0
    middle_count = 0
    for i in range(n - 1):
        for j in range(n//2):
            count += (n - 1 - i) * n - (n - 1 - i + diagonal(i, j))  # 두번째 퀸이 위치할 수 있는 개수
    for i in range(n-1):
        middle_count += (n - 1 - i) * n - (n - 1 - i + diagonal(i, n//2))  # 정가운데 열에서 두번째 퀸이 위치 할 수 있는 개수
    return 2*count+middle_count

n = int(input())
count = 0

if n%2 == 0:
    count = even_Nqueen()
else:
    count = odd_Nqueen()

print(count)

# 첫번째 퀸의 위치를 정하면 두번째 퀸은 전체 체스보드 n*n에서 첫번째 퀸의 위치의 가로(열),세로(행),대각선의 개수를 빼면 된다.
# 첫퀸을 맨위 부터 아래로 돌며 두번째 퀸이 위치할 수 있는 개수를 계속 더해주었다.
# n이 짝수 일때는 첫번째 퀸의 위치가 n//2만큼의 열의 경우만 생각해 2배를 해주면 되고 
# n이 홀수 일때는 n//2만큼의 열의 두배와 정가운데 열인경우를 더해주면 된다.

#시간복잡도
# 결국 첫번째 열 혹은 마지막 열의 대각선개수를 구하는경우가 최악의 경우이다.
# 따라서 모든행에 대한 첫번째 열의 대각선 개수를 구하는데 걸리는 시간은 T(n)=(n-1)+(n-2)+..+1=n(n-1)/2 ==> O(n^2)이다. 즉, (나머지 열들의 대각선 개수 구하는 시간) <= O(n^2)
# 따라서 빅오값은 n//2(열) * n^2(최악의 열 * 모든 행의 대각선 개수) ==> O(n^3)


