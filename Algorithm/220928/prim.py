# 최소신장트리
def prim(r, V):
    MST = [0] * (V+1)   # MST 포함여부
    key = [10000] * (V+1)   # 가중치를 최댓값으로 초기화
    # key[v] => v가 MST에 속한 정점과 연결될 때의 최소 가중치
    key[r] = 0  # 시작지점의 key

    for i in range(V):  # 정점중에 선택
        # MST에 포함되지 않은 정점 중에서 key가 최소인 것 찾기
        # MST[i] == 0 ==> MST에 포함되지 않은 정점
        u = 0
        minV = 10000    # 최소 가중치
        for j in range(V+1):
            if MST[j] == 0  and key[j] < minV: # 아직 고르지 않았고, 가중치가 minV보다 작다면
                u = j
                minV = key[i]
        MST[u] = 1 # 정점 u를 MST에 추가
        # u에 인접한 정점들 v 에 대해서 MST에 포함되지 않은 정점이면,
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])
                # u를 통해서 MST에 포함되는 비용과 기존 비용을 비교해서 최소값을 사용

    return sum(key) # key안에는 가중치들이 들어있게 됨

V, E = map(int, input().split())
adjM = [[0] * (V+1) for _ in range(V+1)]    # 인접행렬
adjL = [[] for _ in range(V+1)]             # 인접 리스트

for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w  # 가중치가 있는 무방향 그래프,
    adjL[u].append((v, w))
    adjL[v].append((u, w))

print(adjM)
print(adjL)

print(prim(0, V))