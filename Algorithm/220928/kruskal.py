
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split())
edge = []
for _ in range(E) :
    u, v, w = map(int, input().split())
    edge.append([w, v, u])
edge.sort() # 가중치를 기준으로 정렬
rep = [i for i in range(V+1)]   # 대표리스트. i의 대표는 i

# MST의 간선 개수 = 정점 수 -1
# N은 정점 개수
N = V + 1
# cnt는 지금까지 선택한 edge 수
cnt = 0
# 가중치의 합
total = 0

# edge를 모두 확인 하면서 하나씩 선택하고,
# 만약 사이클이 생기면 다음거 확인해서 사이클이 안생기는 것만 골라서 추가
for w, v, u in edge:
    if find_set(v) != find_set(u):
        cnt += 1
        union(u, v)
        total += w
        if cnt == N-1 : # MST 구성이 완료되었다.
            break

print(total)
