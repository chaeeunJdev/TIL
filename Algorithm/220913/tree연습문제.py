'''
조건 :
정점 번호 V는 1~(E+1)
간선 수 4 개
부모-자식 순
첫번째 방법 입력 데이터 e, arr
4
1 2 1 3 3 4 3 5
'''
def f(n) :  # global cnt 없이 순회한 정점 수를 리턴하는 함수
    if n == 0 :
        return 0
    else :
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1


E = int(input())    # 정점 개수, 마지막 정점 번호
arr = list(map(int, input().split()))
V = E + 1


# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1) # V번까지 필요한데 0이 있으므로 V+1
ch2 = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1] # 부모, 자식 번호 가져오기
    if ch1[p] == 0:     # 아직 자식이 없으면
        ch1[p] = c      # 첫번째 자식으로 저장
    else :
        ch2[p] = c      # 아니면 두번째 자식으로 저장


# 자식을 인덱스로 부모 번호 저장
# def find_root(V):
#     for i in range(1, V + 1):
#         if par[i] == 0:  # 부모가 없으면
#             return i
#
# par = [0]*(V+1)
# root = find_root(V)


## 서브트리에 속한 정점의 개수 구하기
cnt = 0
print(cnt)
print(f(3))




## cnt를 사용해서 하는 방법!!

def preorder(n):    # 전위순회
    global cnt
    if n :
        cnt += 1   # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])


V = int(input())    # 정점 개수, 마지막 정점 번호
arr = list(map(int, input().split()))
E = V - 1


# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1) # V번까지 필요한데 0이 있으므로 V+1
ch2 = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1] # 부모, 자식 번호 가져오기
    if ch1[p] == 0:     # 아직 자식이 없으면
        ch1[p] = c      # 첫번째 자식으로 저장
    else :
        ch2[p] = c      # 아니면 두번째 자식으로 저장


# 자식을 인덱스로 부모 번호 저장
# def find_root(V):
#     for i in range(1, V + 1):
#         if par[i] == 0:  # 부모가 없으면
#             return i
#
# par = [0]*(V+1)
# root = find_root(V)


## 서브트리에 속한 정점의 개수 구하기
cnt = 0
preorder(3)
print(cnt)


'''
두번째 방법 입력 데이터 v, arr
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''