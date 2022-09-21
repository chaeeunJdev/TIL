def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx] :
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

# 재귀 이용한 버전
def selection_sort2(arr, i) :
    # 재귀적 정의

    # 기저 조건
    if i >= len(arr):
        return
    # 작은 문제의 결과를 통해 큰 문제를 해결하는 유도 조건

    # 현재 위치가 0일 때부터 길이 -1 위치 자리를 찾는다
    # 작은 문제는 현재 위치가 i일때의 그 위치에 맞는 원소를 찾아 자리를 바꾼다.
    min_idx = i # 최소 원소의 위치를 일단 i로 시작
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # =======================================
    # i 다음 위치로 가서 그 위치에 맞는 최소값을 찾아 바꾸는 일을 해야한다.
    selection_sort2(arr, i+1)

arr = [9,5,6,2,3,1,4,8,7,10,0]
selection_sort2(arr, 0)

print(arr)