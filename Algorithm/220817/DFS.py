adjList = [[1, 2],       # 0번 정점에서 인접한 정점의 번호
           [0, 3, 4],   # 1
           [0, 4],      # 2
           [1, 5],      # 3
           [1, 2, 5],   # 4
           [3, 4, 6],   # 5
           [5]]         # 6

def dfs(v, N):
    top = -1
    print(v)

    visited[v] = 1      # 시작점 방문 표시

    while True :
        for w in adjList[v]:
            if visited[w] == 0:     # v의 인접 정점 중 방문 안 한 정점 w 찾기
                top += 1
                stack[top] = v      # push(v)

                v = w               # 다음을 방문할 w를 v에 저장
                print(v)
                visited[w] = 1      # 방문 표시

                break

            else :                  # v의 인접 정점 중 방문 안 한 정점이 없다면
                if top != -1:       # 스택이 비어있지 않은 경우
                    v = stack[top]  # pop
                    top -= 1
                else :              # 스택이 비어있으면
                    break           # while문 종료

N = 7
visited = [0] * N  # visited 생성
stack = [0] * N  # stack 생성
dfs(0, N)