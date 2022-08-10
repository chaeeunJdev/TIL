'''
N = 3
M = 4
# N개의 원소를 갖는 0으로 초기화된 1차원 배열  
arr1 = [0]*N

# 크기가 N*M이고 0으로 초기화된 2차원 배열  
arr2 = [[0]*M for _ in range(N)]


# 2차원 배열 모든 원소의 합 
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N) : 
    for j in range(N):
        s += arr[i][j]
print(s)



# 최대 행의 합
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxV = 0 # 최대 행의 합
for i in range(N):
    rs = 0 # 행의 합
    for j in range(N) :
        rs += arr[i][j]
    if maxV < rs:
        maxV = rs
print(maxV)
'''

# 대각선의 합 4*4
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N) :
    for j in range(N) :
        if i==j:
            s+= arr[i][j]

# 위의 방법과 같은 방법. 결국 i와j가 같은 값이니까 반복문을 하나만써서도 구현이 가능함
s = 0
for i in range(N) :
    s += arr[i][i]


# 반대 대각선의 합 (0,3)(1,2)(2,1)(3,0)
s = 0
for i in range(N):
    s += arr[i][N-1-i]

# 만약 두 방향의 대각선의 합을 더하라는 문제가 나오고 홀수*홀수의 배열일 경우면
# 가운데 값이 겹치기때문에 한번 빼줘야 함 ==> 가운데 값 좌표 = N//2


# (00)(11)(22)(33)대각선을 기준으로 오른쪽 위 칸 들의 합과  왼쪽 아래 칸들의 합 중 더 큰 값
# 오른쪽 칸들은 i < j이고 왼쪽은 i >j가 된다
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s1 = 0
s2 = 0
for i in range(N) :
    for j in range(N):
        if i > j:
            s1 += arr[i][j]
        elif  i < j:
            s2 += arr[i][j]


# 사선의 합
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = [0]*(2*N-1)
for i in range(N) :
    for j in range(N):
        s[i+j] += arr[i][j]
print(s)
