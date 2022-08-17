# 여는괄호는 push
# 닫는괄호는 pop
# input으로 괄호를 입력받고 괄호의 짝을 검사하는 프로그램

def check(bracket) :
    stack = [0]* 10
    top = -1
    for i in bracket :
        if i == "(":
            top += 1
            stack[top] = 1
        else :
            stack[top] = 0
            top -= 1
            if top < -1 :
                return "no"

    print(stack)
    sum_stack = 0
    for v in stack :
        sum_stack += v

    if sum_stack == 0:
        return "yes"
    else :
        return "no"


bracket = input()
print(check(bracket))


# 교수님 방법
bracket = input()
stack = []
answer = 1 # 1은 괄호가 잘 되어있다. 0은 잘 안되어있다.

for c in bracket: # 괄호 문자열에서 괄호를 하나씩 떼오기
    if c == "(":
        # 괄호가 열리면 왼쪽 괄호 추가
        stack.append(c)
    elif c == ")":
        if len(stack) == 0:
            # 괄호가 열린적이 없는데 닫으려고 하는 경우
            answer = 0 # 잘못되었다고 체크하고 break
            break
        # 열린적이 있는 경우 쌍 완성 => 제거
        stack.pop(-1) # 열린 괄호, 닫힌 괄호 쌍 완성
if len(stack) >0: # 스택에 남은 괄호가 있다. => 제대로 괄호가 닫히지 않았따.
    answer = 0

print(answer)