T = int(input())

for test in range(1, T+1):
    N = int(input())
    ai = list(map(int, input()))


    cnt = 0
    max_cnt = 0

    for i in range(N):
        if ai[i] == 1 :
            cnt += 1
            # 0을 만나면 cnt의 값이 다시 0으로 초기화되니까
            # 그 전에 최대 연속 값 max_cnt를 저장
            if cnt >= max_cnt : 
                max_cnt = cnt
        else :
            cnt = 0

    print(f"#{test} {max_cnt}")
