T = 10
for tc in range(1, T+1):
    n = int(input())
    infix = input() # 중위표기법이 사용된 수식 입력

    stack = [0] * n
    top = -1
    icp = {"+" : 1, "*": 2} # 딕셔너리 생성

    postfix = ""     # 후위표기법으로 바뀐 수식을 저장할 변수

    for i in range(n):
        if "0" <= infix[i] <= "9":  # 토큰이 피연산자인 경우
            postfix += infix[i]     # postfix에 push

        else :  # 토큰이 연산자인 경우
            # stack의 top의 우선순위가 stack에 추가하려고하는 연산자의 우선순위보다 높거나 같으면
            # 넣으려고 하는 연산자의 우선순위보다 낮은 연산자를 만날때까지 pop
            if top > -1 and icp[stack[top]] >= icp[infix[i]]:
                postfix += stack[top] # 후위표기법 변수에 저장해주고
                top -= 1 # pop

            top += 1
            stack[top] = infix[i] # i번째 연산자 push

    while top > -1: # 스택이 빌때까지
        postfix += stack[top] # 스택안에 있던 연산자들을 꺼내서 후위표기법 변수에 더해주기
        top -= 1

    c_stack = [] # 후위표기법으로 정리된 수식을 계산할 스택 생성
    for i in range(n):
        if "0" <= postfix[i] <= "9":    # 토큰이 피연산자이면
            c_stack.append(postfix[i])  # 계산 스택에 저장

        else :  # 토큰이 연산자인경우
            if postfix[i] == "+" : # +이면
                A = int(c_stack.pop())  # 값 두개 pop
                B = int(c_stack.pop())
                calculation = B + A     # 연산 순서 중요. 먼저 꺼낸 피연산자가 연산자의 오른쪽에 위치
                c_stack.append(calculation)

            elif postfix[i] == "*" :
                A = int(c_stack.pop())
                B = int(c_stack.pop())
                calculation = B * A
                c_stack.append(calculation)

    ans = c_stack.pop()
    print(f"#{tc} {ans}")
