'''
def f(i, N) :       # i 현재 단계, N 목표 단계
    if i == N:
        return
    else:
        print(i)
        f(i+1, N)

f(0, 3)
'''

# 크기가 N인 배열의 모든 우너소에 접근하는 재귀함수
def f(i, N) :
    if i == N:      # 배열을 벗어남
        return
    else :          # 남은 원소가 있는 경우
        B[i] = A[i] # B에 복사
        f(i+1, N)   # 다음 원소로 이동

N = 3
A = [1, 2, 3]
B = [0]*N
f(0, N)             # 0번 원소부터 N개의 원소에 접근
print(B)


