
def inorder(n):    # 중위순회
    if n :
        inorder(ch1[n])
        print(arr[n-1][1], end="")    # visit(n)
        inorder(ch2[n])

T = 10
for tc in range(1, T+1):
    n = int(input())
    # 부모를 인덱스로 자식 번호 저장
    ch1 = [0] * (n + 1)  # V번까지 필요한데 0이 있으므로 V+1
    ch2 = [0] * (n + 1)
    arr = [list(input().split()) for _ in range(n)]
    for i in range(n):
        if len(arr[i]) == 3:    # 자식이 하나인 경우
            p, c = int(arr[i][0]), int(arr[i][2]) # 부모, 자식 번호 가져오기
            ch1[p] = int(c)      # 첫번째 자식으로 저장

        elif len(arr[i]) == 4:  # 자식이 둘인 경우
            p, c1, c2 = int(arr[i][0]), int(arr[i][2]), int(arr[i][3])
            ch1[p] = c1
            ch2[p] = c2

    print(f"#{tc} ", end="")
    inorder(1)
    print()