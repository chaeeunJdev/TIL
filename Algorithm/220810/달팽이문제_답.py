T = int(input())
for tc in range(1, T+1): 
    N = int(input())

    di = [0, 1, 0, -1] # 우 하 좌 상
    dj = [1, 0, -1, 0]

    d = 0 # 현재 채우고 있는 방향


    snail = [[0]*N for _ in range(N)]

    # 맨 첫칸 (0,0)에 값을 채워놓고 시작  
    value = 1
    ci, cj = 0, 0 # 현재 값을 채울 위치 i행 j열
    snail[ci][cj] = value 

    # 반복을 통해 달팽이를 채워나간다.
    # value가 N*N이 될때까지만 반복

    while value < N*N :
        # 인덱스 범위를 벗어나거나 이미 값이 주어진 경우 방향을 바꿔야 한다.
        # 갈 수 없으면 갈 수 있을때까지 방향을 바꿔보면서 진행 => 방향을 이미 원하는 대로(우 하 좌 상) 설정해놓음
        # 상하좌우가 막혀있다 ==> 값 채우기가 끝났다.

        for i in range(4) : 
            d = (d+i)%4 # 0,1,2,3에서 값이 반복
            
            # 다음 방향으로 출발
            ni = ci + di[d]
            nj = cj + dj[d]  

            if 0 <= ni <N and 0 <= nj < N and snail[ni][nj]==0:
                # 갈수있는 방향을 찾으면 방향 바꾸기를 종료  
                ci = ni
                cj = nj
                break
        
        # 여기까지오면 갈 수 있는 방향을 찾은 것임
        value += 1
        snail[ci][cj] = value

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=" ")
        print() # 한 줄 출력후 줄 바꿈




