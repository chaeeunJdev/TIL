arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

n = len(arr)

comb = [0] * n

cnt = 0

# 조합 으로 풀기
def nCr(n, r, s):
    global cnt
    if r == 0:
        if sum(comb) == 0:
            print(comb)
            cnt+=1
    else:
        for i in range(s, n - r + 1):
            comb[r - 1] = arr[i]
            nCr(n, r - 1, i + 1)

# 0개 선택, 1개 선택, 2개 선택 ... n 개 선택까지
for i in range(n + 1):
    nCr(n, i, 0)

print(cnt)

print("===============================")

# i 하나 하나가 부분집합을 의미한다.
for i in range(1 << n):
    sub = []
    for j in range(n):
        if i & (1 << j):
            # i를 이진수로 바꾸고 j 번째 비트를 확인해 봤더니 1이다 => j 번째 원소가 부분집합에 포함되어 있다.
            sub.append(arr[j])
    # 부분집합의 합을 구해서 그 합이 0이면 출력
    if sum(sub) == 0:
        print(sub)
