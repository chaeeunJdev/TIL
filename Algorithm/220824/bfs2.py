di = [-1,1,0,0]
dj = [0,0,-1,1]

# 2차원 배열을 너비 우선 탐색으로 탐색하는 bfs 함수 작성
def bfs(si, sj, n):
    visited = [[0]* n for _ in range(n)] # 2차원 배열로 방문 체크
    queue = []
    queue.append((si,sj))
    visited[si][sj] = 1
    day = 0

    while queue :
        # 내가 현재 위치에서 방문을 몇번 할건지 구하자
        # 방문할 위치는 큐에 들어있고, 그 위치의 개수(큐의 크기)를 구하면 된다
        size = len(queue)

        # 2차원 배열 모양 출력
        print(f"{day}일차")
        print("========")
        for k in range(n):
            print(visited[k])
        print("========")

        # 탐색 횟수를 이전에 내가 알아낸 큐의 크기만큼만 하도록 제한 하면
        # 해당 일차에만 반복을 하도록 제한 할 수 있다.
        for _ in range(size):
            # 현재 방문 위치 꺼내기
            i, j = queue.pop(0)  # 큐에서 맨 앞의 원소 가져오기. 현재 위치

            # # 2차원 배열 모양 출력
            # print("========")
            # for k in range(n):
            #     print(visited[k])
            # print("========")

            # 현재 위치에서 갈 수 있는 곳 검사 (델타를 이용한 4방향 탐색)
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                # 다음 위치가 탐색이 가능한 위치인지 검사(배열 범위를 벗어나지는 않았는지, 방문을 전에 한 적 이 있는지)
                if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))

        day += 1

n = 10 # 10*10
bfs(5,5,n)

