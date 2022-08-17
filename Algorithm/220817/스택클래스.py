# 스택을 클래스로
class stack :
    def __init__(self):
        self.items=[] # 스택에 사용할 리스트 (저장공간)

    # 1. push 원소 삽입
    # item : 삽입할 원소

    def push(self, item):
        self.items.append(item)
        print(f"push{item}")

    # 2. pop 원소 제거 (꺼내기)
    def pop(self):
        item = self.items.pop(-1)
        print(f"pop {item}")
        return item

    # 3. peek. top에 있는 원소 반환(제거하지 않음)
    def peek(self):
        print(f"peek {self.items[-1]}")
        return self.items[-1]

    # 4. isEmpty 스택이 비어있는지 확인하는 연산, 비어있으면 True
    def isEmpty(self):
        return not self.items

# 스택 생성
my_stack = stack()

# 스택에 원소 삽입
for i in range(5) :
    my_stack.push(i)

# 스택의 꼭대기 (top)에 있는 원소 반환
print(my_stack.peek())

# 스택에서 원소 제거
for i in range(5):
    my_stack.pop()