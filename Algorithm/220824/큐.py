# 선형큐
n = 5
q = [0] * n

front = rear = -1

# q.insert(0,1)

def enQueue(item): # 큐에 원소를 삽입하는 연산, rear 1 씩 증가
    global rear
    # 큐가 만약 꽉차 있다면 삽입 불가 처리
    if isFull():
        print("FULL!")
    # 그게 아니면 rear 를 1 증가시키고, 큐에 원소 삽입
    else:
        rear += 1
        q[rear] = item

def deQueue(): # 큐의 원소를 하나 빼내고 삭제하는ㅌ 연산, front 1씩 증가
    global front
    # 큐가 만약 비어있다면 삭제 불가 처리
    if isEmpty():
        print("EMPTY!")
    # 그게 아니면 front를 1 증가시키고, 큐의 원소 하나 삭제
    else:
        front += 1
        return q[front]

def isFull(): # 큐가 꽉 찼는지 확인해 주는 함수
    return rear == len(q) - 1

def isEmpty(): # 큐가 비어있는지 확인해 주는 함수 (큐안에 들어있는 원소 갯수가 0인지)
    return front == rear



for i in range(5): # 0 ~ 4
    enQueue(i)

print(isFull())
enQueue(5)

for i in range(5):
    print(deQueue())

print(isEmpty())
deQueue()




'''  
rear += 1
q[rear] = 10    # enqueue(10)

rear += 1
q[rear] = 20    # enqueue(20)

rear += 1
q[rear] = 30    # enqueue(30)

rear += 1
q[rear] = 40    # enqueue(40)

front += 1      # dequeue()
print(q[front])

front += 1      # dequeue()
print(q[front])

front += 1      # dequeue()
print(q[front])

# 원형큐
N = 3
q = [0] * N
front = 0
rear= 0

rear += (rear + 1) % N
q[rear] = 10    # enqueue(10)

rear += (rear + 1) % N
q[rear] = 20    # enqueue(20)

rear += (rear + 1) % N
q[rear] = 30    # enqueue(30)

rear += (rear + 1) % N
q[rear] = 40    # enqueue(40)

front += (front + 1) % N      # dequeue()
print(q[front])

front += (front + 1) % N      # dequeue()
print(q[front])

front += (front + 1) % N      # dequeue()
print(q[front])
'''