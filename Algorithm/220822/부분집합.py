# 집합 {1,2,3}의 원소에 대해 각 부분집합에서의 포함 여부를 트리로 표현

def f(i, N):
    global answer
    global cnt
    cnt += 1
    if i == N : # i가 N이되면 함수가 끝났다는 뜻임!
        print(bit)
        s = 0
        for i in range(N) : # 이 아래로 3문장을 쓰면 부분집합을 101의 형태가 아닌 포함된 원소들을
            # 직접 출력 가능
            if bit[i]:
                print(A[i], end= " ")
                s += A[i] # 부분집합의 합 구하기
        if s == 10 :
            answer += 1 # 부분집합의 합이 10인 경우의 수
    else :
        candidate = [0, 1]
        for x in candidate:
            bit[i] = x
            f(i+1, N)

A = [1, 2, 3,4,5,6,7,8,9,10]
bit = [0] * 10
answer = 0
cnt = 0
f(0, 10)
print(answer, cnt)