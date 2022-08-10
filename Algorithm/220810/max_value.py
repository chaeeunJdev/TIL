N = int(input())
numbers = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

max_value = 0

for i in range(N) : 
    for j in range(N) :
        max_value = arr[i][j] if max_value < arr[i][j] else max_value
        