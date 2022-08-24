T = int(input())

for tc in range(1, T+1) :
    arr = list(map(int, input().split()))

    N = len(arr)

    exist = 0 # 부분집합의 합이 0이 될때가 존재하면 1 그게 아니면 0
    for i in range(1, 1<<N): # 공집합을 제외하기 위해서 1부터 시작
        subset_sum = 0
        for j in range(N) : # j = 0, 1, 2,,, N-1
            if i & (i<<j) : 
                # i의 비트를 j와 비교 list의 j번째 인덱스에 있는 원소가
                # 부분집합에 포함되어 있는지 검사
                # arr[j]는 부분집합에 포함되어 있다.
                subset_sum += arr[j] # 부분집합의 합
        exist = 1 if subset_sum ==0 else exist
    
    print(f"#{tc} {exist}")