def fibo(n) :
    if n <2 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)

for i in range(21):
    print(i, fibo(i))


# memo 사용 방법. 훨씬 빠름
def fibo(n) :
    if memo[n] == -1 : # 아직 계산된 적 없는 2번째 인덱스 이상부터
        memo[n] = fibo(n-1) + fibo(n-2)

    return memo[n]
memo = [-1] * 101
memo[0] = 0
memo[1] = 1
for i in range(101):
    print(i, fibo(i))