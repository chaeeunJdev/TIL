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

def deq():
    global last
    tmp = heap[1]   # 루트 원소를 기억해 놓는다.
    # 원소를 삭제하고 나면 루트가 바뀌기 때문에 리턴해줄 값을 미리 저장
    heap[1] = heap[last]    # 마지막 원소를 루트자리에 갖다놓기
    last -= 1   # 개수 감소
    p = 1   # 루트부터 자식과 비교를 시작
    c = p * 2   # 비교할 자식의 위치는 왼쪽부터 확인

    # 자식이 없는 경우 빼고, 자식이 있는 경우 비교 시작
    while c <= last :
        # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면 비교대상을 오른쪽으로 한다.
        # 최소힙인 경우 여기 부등호 바꿔주기
        if c + 1 <= last and heap[c] < heap[c+1]:
            c += 1

        # 최소힙인 경우 여기 부등호 바꿔주기
        if heap[p] < heap[c] :  # 부모가 자식보다 작아버리면 자리를 바꿔줘야 한다.
            heap[p], heap[c] = heap[c], heap[p]
            # 또 계속 바꿔야 하니까, 자식과 부모 교환
            p = c
            c = p * 2
        else :
            # 부모가 더 크면 현재 위치를 찾은거니까 비교 중단
            break

    # 이진 탐색 트리 위치 조정 완료
    return tmp


heap = [0] * 100
last = 0    # 마지막 원소의 위치 ( 삽입할 원소가 올 위치)