N = int(input())
arr = list(map(int, input().split()))
maxIdx = 0
for i in range(1, N):
    if arr[maxIdx] <= arr[i] :
        maxIdx = i
print(maxIdx)