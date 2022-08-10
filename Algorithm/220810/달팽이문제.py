# 2차원 배열을 달팽이 껍질처럼 회전하면서 들어가도록 출력하여라
# swea1954

# 오른쪽, 아래, 왼쪽, 위 (우하좌상) 방향이 반복
# 델타 이용

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    num = 1

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    arr[0][0] = num

    for i in range(N) :
        for j in range(N) :

            for d in range(4):
                ni = i+di[d]
                nj = j+dj[d]
                
                while arr[ni][nj] == 0 and 0 <= ni < N and 0 <= nj < N: 
                    num += 1
                    arr[ni][nj] = num
                    ni = i+di[d]
                    nj = j+dj[d]


