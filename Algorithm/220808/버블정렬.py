N = int(input())
arr = list(map(int, input().split())) 
for i in range(N-1, 0, -1) : # 맨 끝에는 정렬된 원소가 자리하기 때문에 N을 점점 줄이면서 해야함!
    for j in range(i) : 
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)