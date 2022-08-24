# p = 1   # 처음 줄 설 사람 번호
#
# q = []
# N = 20  # 초기 마이쮸 개수
# m = 0   # 나눠준 개수
#
# while m < N: # 아직 마이쮸가 남아있는 경우
#     # input()
#     q.append((p,1,0))   # 처음 줄 서는 사람
#     # print(q)
#     v, c, my = q.pop()
#     # print(f'큐에 있는 사람 수 {len(q)+1}, 받아간 사탕 수{c}, 나눠준 사탕 수{m}')
#     m += c
#     q.append((v, c+1, my+c))    # 마이쮸를 받고 다시 서는 사람
#     p += 1      # 처음 줄서는 사람 번호
# print(f'마지막 받은 사람 : ')



# 교수님 방법
import time
start = time.time()
p = 1   # 처음 줄 설 사람 번호
q = []
N = 1000000  # 초기 마이쮸 개수
m = 0   # 나눠준 개수
v = 0 마지막에 받는 사람은 누구인지?

while m < N: # 아직 마이쮸가 남아있는 경우
    q.append((p,1,0))   # 마이쭈를 받을 사람을 줄에 세운다. (번호표 주기)
    v, c, my = q.pop(0) # pop() => 맨 마지막 원소 / pop(0)=> 첫 번째 원소를 준다
    # print(f'큐에 있는 사람 수 {len(q)+1}, 받아간 사탕 수{c}, 나눠준 사탕 수{m}')
    m += c
    # 마이쭈를 받았으니, 다시 받기위해 줄 맨 뒤로 이동
    q.append((v, c+1, my+c))
    p += 1      # 처음 줄서는 사람 번호
# print(f'마지막 받은 사람 : {v}')

# 종료 시간 측정
print(f"걸린 시간 : {time.time() - start}")

# deque를 이용해서 구현해보기
# from collections import deque
# p = 1
# q = deque()
# n = 1000000
# m = 0
# v = 0
#
# while m <n:
#     q.append((p,1,0))
#     v,b,my = q.popleft() # 맨 왼쪽에서 원소 빼기
#     m += c
#     q.append((v, c+1, my+c))
#     p += 1