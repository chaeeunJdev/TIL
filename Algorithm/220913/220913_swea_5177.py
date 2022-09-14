def enq(n) :
    global last
    last += 1
    heap[last] = n  # heap의 last에 들어온 원소 추가

    # 만약 새로 추가된 원소가 부모 노드보다 더 커버린 경우 자리를 바꿔줘야 한다.
    c = last    # 새로 추가된 노드 (자식노드)
    p = c // 2  # 부모노드

    while p and heap[p] < heap[c] : # 부모노드가 있고 and 부모보다 자식노드의 값이 더 큰 경우
        # 최소힙인 경우는 위에 부등호만 바꿔주면 됨!
        heap[p], heap[c] = heap[c], heap[p] # 자리를 바꿔준다
        # 혹시 바꾸고 난 다음에도 또 바꿔야 할 수도 있으니까
        # 부모와 자식을 바꿔준다.
        c = p
        p = c // 2

def heap_sum(n):
    # 중단 조건
    if n < 1:
        return 0

    # 재귀함수 호출
    result = heap[n]
    # 부모를 계속 거쳐가면서 언젠가 루트 노드에 도착하게 된다.
    return result + heap_sum(n // 2)

T = int(input())
for tc in range(1, T+1):
    n = int(input())    # 노드의 개수
    heap = [0] * (n+1)
    last = 0    # 마지막 원소의 위치 (삽입할 원소가 올 위치)

    # 힙에 삽입할 원소
    numbers = list(map(int, input().split()))

    # 원소를 힙에 차례대로 삽입
    for i in numbers:
        enq(i)
    
    print(f"#{tc} {heap_sum(last // 2)}")    # 조상노드는 자시 자신을 빼야하므로 // 2를 통해 부모노드를 넣기