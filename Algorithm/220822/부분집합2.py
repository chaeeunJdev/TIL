def f(i, N, s, t) : # 이전까지 원소의 합 s, 찾고자 하는 값 t
    global answer
    global cnt
    cnt += 1        # 호출횟수 카운트
    if i == N:
        if s == t:  # 지금까지 구한 원소의 합이 찾고자하는 값이 되면
            answer += 1
        return
    elif s > t:
        return
    else :
        f(i+1, N, s+A[i], t)    # A[i]가 포함된 경우
        f(i+1, N, s, t)         # A[i]가 포함되지 않은 경우



A = [1, 2, 3,4,5,6,7,8,9,10]
bit = [0] * 10
answer = 0
cnt = 0
f(0, 10, 0, 10) # 부분집합의 합이 10인 경우를 찾는다
print(answer, cnt)