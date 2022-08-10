# 연습문제  
T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0,0,-1,1]
    dj = [-1,1,0,0]

    sum_all_abs = 0

    # 행 우선 순회로 i를 고정하고
    # 안에 있는 반복문으로 열 j 순회
    for i in range(N) :
        for j in range(N) : 
            sum_abs = 0 # i, j가 고정되어있을 때 절대값의 합
            for d in range(4):
                ni = i+di[d] # next i
                nj = j+dj[d] # next j

                if 0 <= ni < N and 0 <= nj < N: # i,j가 가장자리쪽에 있는 경우면 4방향의 이웃이 없고 2개밖에 없으므로 유효한지 검사를 해줘야함!!!
                    # ni, nj is valid
                    sum_abs += abs(arr[i][j] - arr[ni][nj])
                    #abs 함수를 사용하지 못하는 경우
                    #sub = arr[i][j] - arr[ni][nj] if arr[i][j] - arr[ni][nj]  > 0 else (arr[i][j] - arr[ni][nj] )* -1
                    #sum_abs += sub
            sum_all_abs += sum_abs

    print(f"#{tc} {sum_all_abs}")