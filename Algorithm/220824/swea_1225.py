for _ in range(10):
    tc = int(input())
    q = list(map(int, input().split()))

    while True :
        for i in range(1, 6):   # 사이클 반복
            a = q[0] - i        # q의 첫값 - i 저장
            q.append(a)         # 맨 뒤에 삽입
            q = q[1::]          # q의 첫번째 원소를 제거한 리스트를 다시 q로 저장

            if q[-1] <= 0:      # q의 마지막 원소가 0보다 작다면
                q[-1] = 0       # 0으로 만들고
                break           # for문 종료

        if q[-1] == 0:          # q의 마지막 원소가 0이라면
            break               # while문 종료
    print(f"#{tc} {' '.join(map(str, q))}")


