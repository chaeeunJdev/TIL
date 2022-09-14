'''
조건 :
정점 번호 V는 1~(E+1)
간선 수 4 개
부모-자식 순
1 2 1 3 3 4 3 5
'''
def preorder(n):    # 전위순회
    if n :
        print(n)    # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):    # 중위순회
    if n :
        inorder(ch1[n])
        print(n)    # visit(n)
        inorder(ch2[n])

def postorder(n):    # 후위순회
    if n :
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)    # visit(n)


E = int(input())
arr = list(map(int, input().split()))
V = E + 1
root = 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1) # V번까지 필요한데 0이 있으므로 V+1
ch2 = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1] # 부모, 자식 번호 가져오기
    if ch1[p] == 0:     # 아직 자식이 없으면
        ch1[p] = c      # 첫번째 자식으로 저장
    else :
        ch2[p] = c      # 아니면 두번째 자식으로 저장

# preorder(root)
# inorder(root)
# postorder(root)

# 자식을 인덱스로 부모 번호 저장
def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면
            return i

par = [0]*(V+1)
root = find_root(V)
print(root)
