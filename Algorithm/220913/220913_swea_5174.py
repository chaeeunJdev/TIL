def preorder(node):
    global count
    count += 1
    if c1[node] != 0:
        preorder(c1[node])
    if c2[node] != 0:
        preorder(c2[node])


T = int(input())

for tc in range(1, T + 1):
    # 간선의 개수, 시작 노드의 번호
    e, n = map(int, input().split())

    # 노드 (트리) 를 표현하기위한 배열
    # 왼쪽
    c1 = [0] * (e + 2)
    # 오른쪽
    c2 = [0] * (e + 2)

    # 간선 정보
    edges = list(map(int, input().split()))
    # 두개씩 끊어서 앞에오는거는 부모노드, 뒤에오는거는 자식노드
    for i in range(0, e * 2, 2):
        p = edges[i]
        c = edges[i + 1]

        # 트리 만들어주기
        # 왼쪽 자식이 없다 => 왼쪽에 추가
        if c1[p] == 0:
            c1[p] = c
        # 왼쪽 자식이 있다 => 오른쪽에 추가
        else:
            c2[p] = c

    # 노드의 개수를 세기 시작
    count = 0
    # 중위순회, 후위순회, 전위순회
    preorder(n)
    print(f"#{tc} {count}")
    # 자식노드가 없으면 탐색을 중지
    # c1[node] != 0 :
    #   preorder(c1[node]) 전위순회의 경우
